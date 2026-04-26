import pandas as pd
from datetime import datetime
from feast import FeatureStore
from sqlalchemy import create_engine

NAME = "energydata_complete_v1"


def send_to_db():
    df = pd.read_csv(f"data/processed/{NAME}.csv")
    df["event_timestamp"] = datetime.now()

    engine = create_engine(
        "postgresql+psycopg2://admin:admin@127.0.0.1:5432/feature_store"
    )

    df.to_sql("iris_table", engine, if_exists="append", index=False)

    print(f"Sent to db {df.shape[0]} objects")


if __name__ == "__main__":
    send_to_db()
