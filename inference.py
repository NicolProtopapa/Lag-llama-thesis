import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression

# 1) Φόρτωση train/test
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

# 2) Διαχωρισμός χαρακτηριστικών (X) και στόχου (y)
X_train = train.drop(columns=["tipo"])
y_train = train["tipo"]

X_test = test.drop(columns=["tipo"])
y_test = test["tipo"]

# 3) Απλό μοντέλο Logistic Regression για baseline
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 4) Προβλέψεις
y_pred = model.predict(X_test)

# 5) Αξιολόγηση
print("----- Ακρίβεια -----")
print(accuracy_score(y_test, y_pred))

print("\n----- Αναφορά ταξινόμησης -----")
print(classification_report(y_test, y_pred))

print("\n----- Πίνακας Σύγχυσης -----")
print(confusion_matrix(y_test, y_pred))
