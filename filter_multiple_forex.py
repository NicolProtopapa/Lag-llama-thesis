import pandas as pd
import os

# Διαβάζουμε το μεγάλο αρχείο
df = pd.read_csv("data/daily_forex_rates.csv")

# Λίστα νομισμάτων που θέλουμε (με βάση το EUR)
currencies = ["USD", "GBP", "JPY", "CHF", "AUD", "CAD", "CNY"]

# Φάκελος εξόδου
output_dir = "data/forex_pairs"
os.makedirs(output_dir, exist_ok=True)

# Για κάθε νόμισμα φτιάχνουμε ξεχωριστό αρχείο
for curr in currencies:
    subset = df[df["currency"] == curr][["date", "currency", "exchange_rate"]]
    subset = subset.sort_values("date")
    
    out_path = os.path.join(output_dir, f"eur{curr.lower()}.csv")
    subset.to_csv(out_path, index=False)
    
    print(f"Αποθηκεύτηκε: {out_path} με {subset.shape[0]} γραμμές")

print("✅ Τελείωσε η δημιουργία των αρχείων!")
