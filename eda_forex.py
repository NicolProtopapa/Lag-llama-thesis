import os
import pandas as pd
import matplotlib.pyplot as plt

# Φάκελοι
input_dir = "data/clean"

# Παίρνουμε όλα τα CSV
files = [f for f in os.listdir(input_dir) if f.endswith(".csv")]

for file in files:
    path = os.path.join(input_dir, file)
    print(f"\nΑνάλυση για: {file}")

    # Διαβάζουμε το dataset
    df = pd.read_csv(path)

    # Βεβαιωνόμαστε ότι η ημερομηνία είναι datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Στατιστικά
    print(df["exchange_rate"].describe())

    # Plot time series
    plt.figure(figsize=(10,4))
    plt.plot(df["date"], df["exchange_rate"], label=file.replace(".csv",""))
    plt.title(f"Συναλλαγματική Ισοτιμία {file.replace('.csv','').upper()}")
    plt.xlabel("Ημερομηνία")
    plt.ylabel("Ισοτιμία")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
