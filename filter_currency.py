import pandas as pd

# Φορτώνουμε όλο το dataset
df = pd.read_csv("data/daily_forex_rates.csv")

# Επιλέγουμε base = EUR
df = df[df["base_currency"] == "EUR"]

# Διάλεξε ποιο νόμισμα θέλεις να φιλτράρεις (π.χ. USD, GBP, JPY)
currency = "USD"   # άλλαξέ το σε "GBP", "JPY", κλπ

filtered = df[df["currency"] == currency][["date", "currency", "exchange_rate"]]
filtered = filtered.sort_values("date")

# Αποθήκευση
out_path = f"data/eur{currency.lower()}_full.csv"
filtered.to_csv(out_path, index=False)

print(f"Αποθηκεύτηκε το EUR/{currency} dataset με σχήμα: {filtered.shape}")
print(filtered.head())
