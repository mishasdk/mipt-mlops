import pandas as pd
import os
import json


NAME = "energydata_complete_v1"


def metrics():
    """
    Шаг 2. Расчет метрик по датасету (аналог describe по колонкам).
    """
    df = pd.read_csv(f"data/processed/{NAME}.csv")

    os.makedirs("data/metrics", exist_ok=True)

    result = {}

    for col in df.columns:
        series = df[col]

        col_metrics = {
            "type": str(series.dtype),
            "count": int(series.count()),
            "missing": int(series.isna().sum()),
        }

        # числовые метрики
        if pd.api.types.is_numeric_dtype(series):
            col_metrics.update({
                "mean": float(series.mean()),
                "std": float(series.std()),
                "min": float(series.min()),
                "25%": float(series.quantile(0.25)),
                "50%": float(series.median()),
                "75%": float(series.quantile(0.75)),
                "max": float(series.max()),
            })
        else:
            # категориальные метрики
            col_metrics.update({
                "unique": int(series.nunique()),
                "top": series.mode().iloc[0] if not series.mode().empty else None,
                "freq": int(series.value_counts().iloc[0]) if not series.empty else 0,
            })

        result[col] = col_metrics

    with open(f"data/metrics/{NAME}.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    metrics()
