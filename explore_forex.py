import pandas as pd

# 1. Φόρτωση του dataset
df = pd.read_csv("data/daily_forex_rates.csv")

# 2. Εμφάνιση βασικών πληροφοριών
print("----- Στήλες -----")
print(df.columns)

print("\n----- Πρώτες γραμμές -----")
print(df.head())

print("\n----- Info -----")
print(df.info())

print("\n----- Unique base currencies -----")
print(df["base_currency"].unique())

print("\n----- Πόσα διαφορετικά νομίσματα έχουμε -----")
print(df["currency"].nunique())

print("\n----- Λίστα με νομίσματα -----")
print(df["currency"].unique()[:20])  # δείχνουμε τα πρώτα 20 για παράδειγμα

# 3. Έλεγχος για missing values
print("\n----- Missing values -----")
print(df.isnull().sum())
