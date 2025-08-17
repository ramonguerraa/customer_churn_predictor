import pandas as pd
from src.config import DATA_RAW, DATA_PROCESSED


def load_data(filepath: str = DATA_RAW) -> pd.DataFrame:
    """
    Load raw churn dataset from a CSV file.
    """
    # Build absolute path relative to project root
    print(f"Loading data from: {filepath}")
    return pd.read_csv(filepath)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic cleaning operations on the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Raw dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned dataset after preprocessing.
    """
    df_clean = df.dropna().drop_duplicates()
    return df_clean

def save_clean_data(df: pd.DataFrame, filepath: str = DATA_PROCESSED):
    """
    Save the cleaned dataset to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataset.
    filepath : str, optional
        Path to save the cleaned dataset (default: data/processed/churn_clean.csv).
    """
    print(f"Saving cleaned data to: {filepath}")
    df.to_csv(filepath, index=False)
