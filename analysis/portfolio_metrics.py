import pandas as pd
import os
import numpy as np

pred_folder = "predictions"

returns = []

for file in os.listdir(pred_folder):

    if file.endswith("_predictions.csv"):

        df = pd.read_csv(os.path.join(pred_folder, file))

        df['return'] = df['prediction'].pct_change()

        returns.extend(df['return'].dropna().tolist())

returns = np.array(returns)

avg_return = np.mean(returns)
volatility = np.std(returns)

sharpe_ratio = avg_return / volatility if volatility != 0 else 0

print("Average Return:", round(avg_return,6))
print("Volatility:", round(volatility,6))
print("Sharpe Ratio:", round(sharpe_ratio,3))