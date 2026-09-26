from pathlib import Path

import pandas as pd


def standardize_train_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize data types for the training sales dataset.

    The function does not apply business-rule cleaning such as
    removing rows or imputing missing values.
    """

    df = df.copy()

    # Convert date from text to pandas datetime.
    df["date"] = pd.to_datetime(df["date"])

    # Standardize numeric identifier fields.
    df["id"] = df["id"].astype("int64")
    df["store_nbr"] = df["store_nbr"].astype("int64")

    # Standardize product-family text field.
    df["family"] = df["family"].astype("string")

    # Standardize forecasting target.
    df["sales"] = df["sales"].astype("float64")

    # Standardize promotion count.
    df["onpromotion"] = df["onpromotion"].astype("int64")

    return df


def standardize_transactions_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize data types for the transactions dataset.

    No rows are removed and no missing values are imputed.
    """
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["store_nbr"] = df["store_nbr"].astype("int64")
    df["transactions"] = df["transactions"].astype("int64")

    return df


def standardize_stores_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize data types for the store master dataset.

    No business-rule cleaning is performed.
    """
    df = df.copy()

    df["store_nbr"] = df["store_nbr"].astype("int64")
    df["city"] = df["city"].astype("string")
    df["state"] = df["state"].astype("string")
    df["type"] = df["type"].astype("string")
    df["cluster"] = df["cluster"].astype("int64")

    return df


def standardize_holidays_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize data types for the holidays/events dataset.

    No duplicate-date handling or event aggregation is performed here.
    """
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["type"] = df["type"].astype("string")
    df["locale"] = df["locale"].astype("string")
    df["locale_name"] = df["locale_name"].astype("string")
    df["description"] = df["description"].astype("string")
    df["transferred"] = df["transferred"].astype("boolean")

    return df


def standardize_oil_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize data types for the oil-price dataset.

    Missing oil prices are preserved for later treatment.
    """
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["dcoilwtico"] = df["dcoilwtico"].astype("float64")

    return df
