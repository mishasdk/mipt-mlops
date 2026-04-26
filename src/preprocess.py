import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder


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

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(df["variety"])
    df["variety"] = y_encoded

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(f"data/processed/{NAME}.csv", index=False)


if __name__ == "__main__":
    preprocess()
