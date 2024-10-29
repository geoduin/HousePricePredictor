from sklearn.preprocessing import OrdinalEncoder
from pandas import DataFrame

def convert_to_numeric(data: DataFrame, mapping: list, column_name: str):
    
    encoder = OrdinalEncoder(categories=mapping)
    
    data[column_name] = encoder.fit_transform(data[column_name])
    data.head()
    return data
