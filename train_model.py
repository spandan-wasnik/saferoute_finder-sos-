"""
train_model.py
--------------
Trains a RandomForest risk-score model using real crime data.

Usage:
    python train_model.py

Output:
    crime_model.pkl
    crime_data.pkl
"""

import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


# ── 1. Train ──────────────────────────────────────────────────────────────────

def train(df):
    X = df[["Latitude", "Longitude", "hour", "day", "month"]].values
    y = df["risk_score"].values

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=120,
        max_depth=10,
        min_samples_leaf=4,
        n_jobs=-1,
        random_state=42
    )

    model.fit(X_tr, y_tr)

    preds = model.predict(X_te)

    print(f"  MAE : {mean_absolute_error(y_te, preds):.4f}")
    print(f"  R²  : {r2_score(y_te, preds):.4f}")

    return model


# ── 2. Main ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  SafeRoute AI — Crime Model Trainer")
    print("=" * 55)

    print("\nLoading dataset …")
    df = pd.read_csv("final_crimeset.csv")

    print(f"  Dataset shape : {df.shape}")

    # ✅ Clean data
    df = df.dropna()

    # ✅ Ensure correct columns
    required_cols = ["Latitude", "Longitude", "hour", "day", "month", "risk_score"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError("CSV format incorrect. Required columns missing.")

    print("\nTraining RandomForest …")
    model = train(df)

    # 💾 Save model
    joblib.dump(model, "crime_model.pkl")
    print("Saved → crime_model.pkl")

    # 💾 Save heatmap data
    heatmap = df[["Latitude", "Longitude", "risk_score"]].sample(
        n=min(3000, len(df)), random_state=42
    ).values.tolist()

    joblib.dump(heatmap, "crime_data.pkl")
    print(f"Saved → crime_data.pkl  ({len(heatmap)} heatmap points)")

    # 🧪 Sanity predictions (using YOUR data scale now)
    print("\nSanity predictions:")
    sample_points = df.sample(3, random_state=42)

    for _, row in sample_points.iterrows():
        risk = model.predict(np.array([[
            row["Latitude"],
            row["Longitude"],
            row["hour"],
            row["day"],
            row["month"]
        ]]))[0]

        print(f"  Lat: {row['Latitude']:.4f}, Lon: {row['Longitude']:.4f} → risk = {risk:.3f}")

    print("\nDone! Run: uvicorn main:app --reload")