import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
IN_FILE  = DATA_DIR / "eurusd_clean.csv"   # από το προηγούμενο βήμα
TRAIN_OUT = DATA_DIR / "train.csv"
TEST_OUT  = DATA_DIR / "test.csv"

# 1) Φόρτωση
df = pd.read_csv(IN_FILE)

# 2) Βρες/ταξινόμησε με βάση ημερομηνία (αν υπάρχει)
date_candidates = ["date", "Date", "DATE", "datetime", "Datetime", "time", "Time", "timestamp", "Timestamp"]
date_col = next((c for c in df.columns if c in date_candidates), None)

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.sort_values(by=date_col).reset_index(drop=True)

# 3) Βεβαιώσου ότι υπάρχει ο στόχος 'tipo'
if "tipo" not in df.columns:
    raise ValueError(f"Δεν βρέθηκε στήλη 'tipo'. Βρέθηκαν στήλες: {list(df.columns)}")

# 4) Χρονολογικό split 80/20
split_idx = int(len(df) * 0.8)
train = df.iloc[:split_idx].copy()
test  = df.iloc[split_idx:].copy()

# 5) Αποθήκευση
train.to_csv(TRAIN_OUT, index=False)
test.to_csv(TEST_OUT, index=False)

# 6) Γρήγορος έλεγχος
def dist(s):
    vc = s.value_counts()
    pct = s.value_counts(normalize=True).round(3)
    return pd.DataFrame({"count": vc, "ratio": pct})

print("Σχήματα:")
print(f"  train: {train.shape}")
print(f"  test : {test.shape}\n")

print("Κατανομή 'tipo' στο train:")
print(dist(train["tipo"]), "\n")

print("Κατανομή 'tipo' στο test:")
print(dist(test["tipo"]))