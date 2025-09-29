import os
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# -------- Δημιουργία sequences --------
def create_sequences(data, seq_length=30):
    xs, ys = [], []
    for i in range(len(data) - seq_length):
        x = data[i:(i + seq_length)]
        y = data[i + seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

# -------- Ορισμός LSTM --------
class LSTMModel(nn.Module):
    def __init__(self, input_size=1, hidden_size=50, num_layers=2):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])  # τελευταίο βήμα
        return out

# -------- Εκπαίδευση & Αξιολόγηση --------
def train_and_evaluate(train_file, test_file, seq_length=30, epochs=15):

    # 1. Φόρτωση δεδομένων
    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    train_values = train_df["exchange_rate"].values
    test_values = test_df["exchange_rate"].values

    # 2. Sequences
    X_train, y_train = create_sequences(train_values, seq_length)
    X_test, y_test = create_sequences(test_values, seq_length)

    X_train = torch.tensor(X_train, dtype=torch.float32).unsqueeze(-1)
    y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(-1)
    X_test = torch.tensor(X_test, dtype=torch.float32).unsqueeze(-1)
    y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(-1)

    train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=32, shuffle=True)

    # 3. Μοντέλο
    model = LSTMModel()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # 4. Εκπαίδευση
    for epoch in range(epochs):
        model.train()
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
        print(f"{os.path.basename(train_file)} - Epoch {epoch+1}/{epochs}, Loss: {loss.item():.6f}")

    # 5. Πρόβλεψη
    model.eval()
    with torch.no_grad():
        y_pred = model(X_test).numpy()

    # 6. Metrics
    mse = mean_squared_error(y_test.numpy(), y_pred)
    mae = mean_absolute_error(y_test.numpy(), y_pred)
    print(f"Αποτελέσματα για {os.path.basename(train_file)}:")
    print(f"MSE: {mse:.6f}, MAE: {mae:.6f}")

    # 7. Γράφημα
    plt.figure(figsize=(10,6))
    plt.plot(y_test.numpy(), label="Πραγματικές")
    plt.plot(y_pred, label="Προβλέψεις")
    plt.legend()
    plt.title(f"LSTM Πρόβλεψη {os.path.basename(train_file).replace('.csv','').upper()}")
    plt.savefig(f"outputs/lstm_{os.path.basename(train_file).replace('.csv','')}.png")
    plt.close()

    return mse, mae

# -------- Κύριο Loop --------
if __name__ == "__main__":
    train_dir = "data/train"
    test_dir = "data/test"
    os.makedirs("outputs", exist_ok=True)

    results = {}

    for file in os.listdir(train_dir):
        if file.endswith(".csv"):
            train_file = os.path.join(train_dir, file)
            test_file = os.path.join(test_dir, file)
            mse, mae = train_and_evaluate(train_file, test_file)
            results[file] = {"MSE": mse, "MAE": mae}

    print("\n===== Συνοπτικά Αποτελέσματα =====")
    for k, v in results.items():
        print(f"{k}: MSE={v['MSE']:.6f}, MAE={v['MAE']:.6f}")
