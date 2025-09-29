import os
import pandas as pd

# Φάκελοι εισόδου/εξόδου
input_dir = "data/clean"
train_dir = "data/splits/train"
test_dir = "data/splits/test"
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Παίρνουμε όλα τα καθαρισμένα CSV
files = [f for f in os.listdir(input_dir) if f.endswith(".csv")]

for file in files:
    path = os.path.join(input_dir, file)
    df = pd.read_csv(path)
    
    # Split 80/20
    split_idx = int(len(df) * 0.8)
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    
    # Αποθήκευση
    base_name = file.replace(".csv", "")
    train.to_csv(os.path.join(train_dir, f"{base_name}_train.csv"), index=False)
    test.to_csv(os.path.join(test_dir, f"{base_name}_test.csv"), index=False)
    
    print(f"Διαχωρίστηκε {file}: train {train.shape[0]} γραμμές, test {test.shape[0]} γραμμές")

print("Τελείωσε ο διαχωρισμός όλων των αρχείων!")
