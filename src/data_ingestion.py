import pandas as pd
from src.config import DATA_PATH

def load_data(file_name):
    """ Load CSV file into a DataFrame"""
    return pd.read_csv(f"{DATA_PATH}/{file_name}")

def clean_data(df):
    """ Simple cleaning operations: fill missing values """
    return df.fillna('')