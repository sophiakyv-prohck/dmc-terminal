# Placeholder capstone script, swap in real analysis once decided.
import pandas as pd

RUN_LABEL = "baseline"   # Question 7: edit this line on both branches

DATA_PATH = "data/big_dataset.csv"
N_ROWS = 6  # try changing this

df = pd.read_csv(DATA_PATH)
print(f"[{RUN_LABEL}]")
print(df.head(N_ROWS))
