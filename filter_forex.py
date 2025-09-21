import pandas as pd

# Φορτώνουμε το μεγάλο dataset
df = pd.read_csv("data/daily_forex_rates.csv")

# Φιλτράρουμε μόνο EUR/USD
eurusd = df[df["currency"] == "USD"]

# Κρατάμε μόνο τις σημαντικές στήλες
eurusd = eurusd[["date", "currency", "exchange_rate"]]

# Αποθηκεύουμε το νέο dataset
eurusd.to_csv("data/eurusd_full.csv", index=False)

print("Αποθηκεύτηκε το EUR/USD dataset με σχήμα:", eurusd.shape)
print(eurusd.head())
