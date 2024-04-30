from typing import List

import pandas as pd
from app.domains.models import Legislator, LegislatorVotes
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


def get_data_results() -> List[LegislatorVotes]:
    legislator_votes: List[LegislatorVotes] = []

    # read all csv files
    legislators = pd.read_csv(LEGISLATORS_DATA, nrows=100, usecols=["id", "name"])
    vote_results = pd.read_csv(VOTES_RESULTS_DATA, nrows=100, index_col=["id"])

    results = legislators.merge(vote_results, left_on="id", right_on="legislator_id")
    for _, row in results.iterrows():
        supported_bills = vote_results.query(
            f"(vote_type == 1) & (legislator_id == {row['id']})"
        ).value_counts()

        opposed_bills = vote_results.query(
            f"(vote_type == 2) & (legislator_id == {row['id']})"
        ).value_counts()

        legislator_votes.append(
            LegislatorVotes(
                id=row["id"],
                legislator=row["name"],
                supported_bills=supported_bills.mean(),
                opposed_bills=opposed_bills.mean(),
            )
        )

    return legislator_votes
