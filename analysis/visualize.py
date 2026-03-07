import pandas as pd
import matplotlib.pyplot as plt
import os

data_folder = "data"
pred_folder = "predictions"

for file in os.listdir(pred_folder):

    if file.endswith("_predictions.csv"):

        stock = file.split("_")[0]

        pred = pd.read_csv(os.path.join(pred_folder, file))
        actual = pd.read_csv(os.path.join(data_folder, stock + ".csv"))

        actual.columns = actual.columns.str.lower()

        actual = actual[['date','close']]
        pred = pred[['date','prediction']]

        merged = pd.merge(actual, pred, on="date")

        plt.figure(figsize=(10,5))
        plt.plot(merged['close'], label="Actual Price")
        plt.plot(merged['prediction'], label="Predicted Price")

        plt.title(stock + " Prediction vs Actual")
        plt.legend()

        plt.savefig(stock + "_prediction_chart.png")

        print(stock + " chart generated")

plt.show()