from pandas import DataFrame
import pandas as pd 

def setup_data(training_path: str, test_path: str):
    training_set = pd.read_csv(training_path)
    test_set = pd.read_csv(test_path)
    return training_set, test_set

def after_filtering(df: DataFrame, useless_columns: list, target: list):
    original_columns = df.columns

    new_columns = [col for col in original_columns if col not in useless_columns and col in target]
    print(new_columns)
    return df[new_columns]