import os
import pandas as pd

# Φάκελοι εισόδου/εξόδου
input_dir = "data/forex_pairs"
output_dir = "data/clean"
os.makedirs(output_dir, exist_ok=True)

# Παίρνουμε όλα τα CSV
files = [f for f in os.listdir(input_dir) if f.endswith(".csv")]

for file in files:
    path = os.path.join(input_dir, file)
    print(f" Καθαρίζουμε: {file}")

    # Διαβάζουμε το CSV
    df = pd.read_csv(path)

    # Μετατροπή ημερομηνίας
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Sort by date
    df = df.sort_values("date")

    # Αφαίρεση duplicates
    df = df.drop_duplicates(subset=["date"])

    # Resample σε daily frequency (fill κενά με forward fill)
    df = df.set_index("date").resample("D").ffill().reset_index()

    # Αποθήκευση σε νέο φάκελο
    out_path = os.path.join(output_dir, file)
    df.to_csv(out_path, index=False)
    print(f"Αποθηκεύτηκε: {out_path} με {len(df)} γραμμές")

print("Τελείωσε το cleaning όλων των αρχείων!")
