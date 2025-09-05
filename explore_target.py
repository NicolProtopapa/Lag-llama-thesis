import pandas as pd
import matplotlib.pyplot as plt

# Φόρτωση του καθαρισμένου dataset
df = pd.read_csv('C:/Users/nikol/Desktop/Thesis/lag-llama-main/data/eurusd_clean.csv')


# ----- Κατανομή τιμών στη στήλη στόχου -----
print("----- Κατανομή στόχου 'tipo' -----")
print(df['tipo'].value_counts())

# ----- Σχετική κατανομή (ποσοστά) -----
print("\n----- Ποσοστά στόχου 'tipo' -----")
print(df['tipo'].value_counts(normalize=True))

# ----- Γραφική απεικόνιση -----
plt.figure(figsize=(5,4))
df['tipo'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Κατανομή τιμών της μεταβλητής στόχου 'tipo'")
plt.xlabel("Τιμή")
plt.ylabel("Πλήθος")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
