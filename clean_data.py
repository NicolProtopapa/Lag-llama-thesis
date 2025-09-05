import pandas as pd

# Φόρτωση του αρχείου CSV
df = pd.read_csv('C:/Users/nikol/Desktop/Thesis/lag-llama-main/data/eurusd.csv')

# ----- Έλεγχος για κενές τιμές -----
print("----- Κενές τιμές ανά στήλη -----")
print(df.isnull().sum())

# ----- Αφαίρεση γραμμών με NaN (αν υπάρχουν) -----
df_clean = df.dropna()

# ----- Έλεγχος για διπλότυπα -----
print("\n----- Πλήθος διπλότυπων γραμμών -----")
print(df_clean.duplicated().sum())

# ----- Αφαίρεση διπλότυπων -----
df_clean = df_clean.drop_duplicates()

# ----- Σώσε τα καθαρισμένα δεδομένα -----
df_clean.to_csv('data/eurusd_clean.csv', index=False)
print("\n✔️ Καθαρισμένα δεδομένα αποθηκεύτηκαν ως 'eurusd_clean.csv'")
