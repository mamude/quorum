from typing import List

import pandas as pd
from app.domains.models import Legislator
from app.utils.csv_paths import LEGISLATORS_DATA


def get_data_legislators() -> List[Legislator]:
    legislators: List[Legislator] = []
    data = pd.read_csv(LEGISLATORS_DATA, usecols=["id", "name"], chunksize=1000)
    for idx, chunk in enumerate(data):
        if idx == 0:
            df = pd.DataFrame(chunk)
            for _, row in df.iterrows():
                legislators.append(Legislator(id=row["id"], name=row["name"]))
        else:
            break
    return legislators
