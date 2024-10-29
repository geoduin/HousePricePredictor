from pandas import DataFrame
import pandas as pd 
def setup_data(training_path: str, test_path: str):
    training_set = pd.read_csv(training_path)
    test_path = pd.read_csv(test_path)
    return training_path, test_path

def after_filtering(df: DataFrame, useless_columns: list):
    return df