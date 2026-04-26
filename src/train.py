import mlflow
import mlflow.sklearn
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score


def train():
    """
    Шаг 3. Обучение классификатора на датасете с ирисами.
    """
    df = pd.read_csv("data/processed/energydata_complete_v1.csv")

    X = df.drop(columns=["variety"])
    y = df["variety"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    mlflow.set_experiment("iris")

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        model.fit(X_train, y_train)

        train_preds = model.predict(X_train)

        train_acc = accuracy_score(y_train, train_preds)
        train_recall = recall_score(y_train, train_preds, average="macro")
        train_f1 = f1_score(y_train, train_preds, average="macro")

        test_preds = model.predict(X_test)

        test_acc = accuracy_score(y_test, test_preds)
        test_recall = recall_score(y_test, test_preds, average="macro")
        test_f1 = f1_score(y_test, test_preds, average="macro")

        mlflow.log_param("model", "RandomForest")
        mlflow.log_param("n_estimators", 100)

        mlflow.log_metric("train_accuracy", train_acc)
        mlflow.log_metric("train_recall", train_recall)
        mlflow.log_metric("train_f1", train_f1)

        mlflow.log_metric("test_accuracy", test_acc)
        mlflow.log_metric("test_recall", test_recall)
        mlflow.log_metric("test_f1", test_f1)

        mlflow.sklearn.log_model(model, "model")
    
    os.makedirs("data/models", exist_ok=True)
    joblib.dump(model, "data/models/iris_classifier.pkl")


if __name__ == "__main__":
    train()
