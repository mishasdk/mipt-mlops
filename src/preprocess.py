import pandas as pd
import os


NAME = "energydata_complete_v1"


def preprocess():
    """
    Шаг 1. Препроцессинг датасета.
    """
    df = pd.read_csv(f"data/raw/{NAME}.csv")

    df = df.rename(columns={
        "Unnamed: 0": "id",
        "sepal.length": "sepal_length",
        "sepal.width": "sepal_width",
        "petal.length": "petal_length",
        "petal.width": "petal_width",
    })

    df = df.dropna()
    df = df.drop_duplicates()

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(f"data/processed/{NAME}.csv", index=False)


if __name__ == "__main__":
    preprocess()
