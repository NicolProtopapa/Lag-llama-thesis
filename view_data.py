import pandas as pd

# Φόρτωση του dataset
df = pd.read_csv('C:/Users/nikol/Desktop/Thesis/lag-llama-main/data/eurusd.csv')


# Εμφάνιση πρώτων γραμμών
print("----- Πρώτες γραμμές του dataset -----")
print(df.head())

# Περιγραφικά στατιστικά
print("\n----- Περιγραφικά στατιστικά -----")
print(df.describe(include='all'))

# Ονόματα στηλών
print("\n----- Ονόματα στηλών -----")
print(df.columns.tolist())


