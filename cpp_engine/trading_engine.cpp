#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

struct Prediction {
    string date;
    double value;
};

vector<Prediction> loadPredictions(const string& filePath) {
    vector<Prediction> data;
    ifstream file(filePath);
    string line;

    getline(file, line); // skip header

    while (getline(file, line)) {
        stringstream ss(line);
        string date, value;

        getline(ss, date, ',');
        getline(ss, value, ',');

        data.push_back({date, stod(value)});
    }

    return data;
}

double simulateTrading(const vector<Prediction>& data) {
    double capital = 10000.0;

    for (size_t i = 1; i < data.size(); i++) {
        if (data[i].value > data[i-1].value) {
            capital *= 1.01;
        } else {
            capital *= 0.99;
        }
    }

    return capital;
}

int main() {

    vector<string> files = {
        "predictions/AAPL_predictions.csv",
        "predictions/AMZN_predictions.csv",
        "predictions/GOOG_predictions.csv",
        "predictions/MSFT_predictions.csv",
        "predictions/NVDA_predictions.csv",
        "predictions/META_predictions.csv",
        "predictions/TSLA_predictions.csv"
    };

    for (string file : files) {

        vector<Prediction> data = loadPredictions(file);

        double finalCapital = simulateTrading(data);

        cout << file << " -> Final Capital: $" << finalCapital << endl;
    }

    return 0;
}