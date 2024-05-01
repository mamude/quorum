from typing import List

import pandas as pd
from app.domains.models import BillVotes, Legislator, LegislatorVotes
from app.utils.csv_paths import (
    BILLS_DATA,
    LEGISLATORS_DATA,
    VOTES_DATA,
    VOTES_RESULTS_DATA,
)


def get_data_legislators() -> List[Legislator]:
    legislators: List[Legislator] = []
    data = pd.read_csv(
        LEGISLATORS_DATA, usecols=["id", "name"], chunksize=1000, index_col=False
    )
    for idx, chunk in enumerate(data):
        if idx == 0:
            df = pd.DataFrame(chunk)
            for _, row in df.iterrows():
                legislators.append(Legislator(id=row["id"], name=row["name"]))
        else:
            break
    return legislators


def get_data_legislators_votes() -> List[LegislatorVotes]:
    legislator_votes: List[LegislatorVotes] = []

    # read all csv files
    legislators = pd.read_csv(LEGISLATORS_DATA, nrows=100, usecols=["id", "name"])
    vote_results = pd.read_csv(VOTES_RESULTS_DATA, nrows=100, index_col=["id"])

    # merge data model
    legislators = legislators.merge(
        vote_results, left_on="id", right_on="legislator_id"
    )

    # group by
    legislators_grouped = (
        legislators.sort_values(by="name").groupby(["name", "id"]).groups
    )

    for row in legislators_grouped.items():
        supporters = legislators.query(
            f"(vote_type == 1) & (legislator_id == {row[0][1]})"
        ).value_counts()
        opposers = legislators.query(
            f"(vote_type == 2) & (legislator_id == {row[0][1]})"
        ).value_counts()

        legislator_votes.append(
            LegislatorVotes(
                id=row[0][1],
                legislator=row[0][0],
                supported_bills=supporters.mean(),
                opposed_bills=opposers.mean(),
            )
        )

    return legislator_votes


def get_data_bills_votes():
    bill_votes: List[BillVotes] = []

    # read all csv files
    bills = pd.read_csv(BILLS_DATA, nrows=100, usecols=["id", "title", "sponsor_id"])
    votes = pd.read_csv(VOTES_DATA, nrows=100, usecols=["id", "bill_id"])
    vote_results = pd.read_csv(VOTES_RESULTS_DATA, nrows=100, index_col=["id"])

    # merge data model
    bills = bills.merge(votes, left_on="id", right_on="bill_id")
    bills = bills.merge(vote_results, left_on="id_y", right_on="vote_id")

    # group by
    bill_grouped = bills.groupby(["id_x", "title", "sponsor_id"]).groups

    for row in bill_grouped.items():
        supporters = bills.query(
            f"vote_type == 1 & bill_id == {row[0][0]}"
        ).value_counts()
        supporters = supporters.groupby("vote_id").sum()

        opposers = bills.query(
            f"vote_type == 2 & bill_id == {row[0][0]}"
        ).value_counts()
        opposers = opposers.groupby("vote_id").sum()

        bill_votes.append(
            BillVotes(
                id=row[0][0],
                bill=row[0][1],
                supporters=supporters.mean(),
                opposors=opposers.mean(),
                primary_sponsor=row[0][2],
            )
        )

    return bill_votes
