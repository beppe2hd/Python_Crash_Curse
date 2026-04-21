import pandas as pd

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def clean_data(df):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "price", "quantity"])
    return df

def add_features(df):
    df["revenue"] = df["price"] * df["quantity"]
    return df

def summary_by_product(df):
    return (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def summary_by_month(df):
    monthly = (
        df
        .set_index("date")
        .resample("M")["revenue"]
        .sum()
    )
    return monthly

def main():
    csv_path = "data_1.csv"
    df = load_data(csv_path)
    df = clean_data(df)
    df = add_features(df)

    print("Ricavi per prodotto:")
    print(summary_by_product(df))

    print("\nRicavi per mese:")
    print(summary_by_month(df))

if __name__ == "__main__":
    main()

