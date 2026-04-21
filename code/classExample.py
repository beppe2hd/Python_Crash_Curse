import pandas as pd

class SalesDataAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.csv_path)
        return self

    def clean_data(self):
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df = self.df.dropna(subset=["date", "price", "quantity"])
        return self

    def add_features(self):
        self.df["revenue"] = self.df["price"] * self.df["quantity"]
        return self

    def summary_by_product(self):
        return (
            self.df.groupby("product")["revenue"]
            .sum()
            .sort_values(ascending=False)
        )

    def summary_by_month(self):
        monthly = (
            self.df
            .set_index("date")
            .resample("M")["revenue"]
            .sum()
        )
        return monthly


analyzer = (
    SalesDataAnalyzer("data_1.csv")
    .load_data()
    .clean_data()
    .add_features()
)

print("Ricavi per prodotto:")
print(analyzer.summary_by_product())

print("\nRicavi per mese:")
print(analyzer.summary_by_month())