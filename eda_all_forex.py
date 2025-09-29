import os
import pandas as pd
import matplotlib.pyplot as plt

# Φάκελοι
input_dir = "data/clean"
output_dir = "outputs/eda_plots"
os.makedirs(output_dir, exist_ok=True)

# Διατρέχουμε όλα τα csv
for file in os.listdir(input_dir):
    if file.endswith(".csv"):
        path = os.path.join(input_dir, file)
        df = pd.read_csv(path, parse_dates=["date"])

        print(f"\n--- Ανάλυση για: {file} ---")
        print(df["exchange_rate"].describe())

        # Γράφημα
        plt.figure(figsize=(10, 5))
        plt.plot(df["date"], df["exchange_rate"], label=file.replace(".csv", ""))
        plt.title(f"Συναλλαγματική Ισοτιμία {file.replace('.csv', '').upper()}")
        plt.xlabel("Ημερομηνία")
        plt.ylabel("Ισοτιμία")
        plt.legend()
        plt.grid(True)

        # Αποθήκευση plot
        plot_path = os.path.join(output_dir, f"{file.replace('.csv','')}.png")
        plt.savefig(plot_path)
        plt.close()

print("\nΟλοκληρώθηκε η EDA για όλα τα νομισματικά ζεύγη.")
