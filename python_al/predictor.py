import os
import pandas as pd
from sklearn.linear_model import LinearRegression

data_folder = "data"
output_folder = "predictions"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(data_folder):

    if file.endswith(".csv"):

        path = os.path.join(data_folder, file)

        df = pd.read_csv(path)

        # normalize column names
        df.columns = df.columns.str.lower()

        # use correct columns
        df = df[['date','close']]

        df['target'] = df['close'].shift(-1)

        df = df.dropna()

        X = df[['close']]
        y = df['target']

        model = LinearRegression()
        model.fit(X, y)

        predictions = model.predict(X)

        df['prediction'] = predictions

        stock_name = file.split(".")[0]

        output_file = os.path.join(output_folder, stock_name + "_predictions.csv")

        df[['date','prediction']].to_csv(output_file, index=False)

        print(stock_name + " processed")

print("All stocks processed successfully.")