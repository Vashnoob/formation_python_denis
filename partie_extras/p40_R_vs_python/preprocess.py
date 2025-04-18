import pandas as pd

# Nettoyage simple : normalisation
df = pd.read_csv("data_raw.csv")
df["y_norm"] = (df["y"] - df["y"].mean()) / df["y"].std()

df.to_csv("data_clean.csv", index=False)
