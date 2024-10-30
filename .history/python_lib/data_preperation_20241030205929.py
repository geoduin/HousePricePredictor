from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from pandas import DataFrame

mappingBsmtExp = ["NA", "No", "Mn", "Av", "Gd"]
mapBsmtFinT1 = ["NA", "Unf", "LwQ", "Rec", "BLQ", "ALQ", "GLQ"]
mappingExtQual = ["Po","Fa", "TA", "Gd","Ex" ]
mapFence = ["NA", "MnWw", "GdWo", "MnPrv", "GdPrv"]
mapFireQu = ["NA", "Po", "Fa", "TA", "Gd", "Ex"]
mapGarageFin = ["NA", "Unf", "RFn", "Fin"]
mapBsmntQu = ["NA", "Po", "Fa", "TA", "Gd", "Ex"]

mapHeatQC = ["Po", "Fa", "TA", "Gd", "Ex"]
mapKitchQual = ["Po", "Fa", "TA", "Gd", "Ex"]
mapLotShape = ["IR3", "IR2", "IR1", "Reg"]
mapPoolQc = ["NA", "Fa", "TA", "Gd", "Ex"]

def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    
    return df

def remove_outliers(df):
    # Outliers verwijderen, mits het aantal niet te groot is.
    return df[
        (df['GrLivArea'] < 4000) &
        (df['OverallQual'] > 1) &
        (df['TotRmsAbvGrd'] < 11) &
        (df['GarageCars'] < 4)
    ]

def encode_categorical_data(df: DataFrame):
    df = get_ordinal(df, "KitchenQual", mapKitchQual)
    df = get_ordinal(df, "ExterQual", mappingExtQual)
    df = get_ordinal(df, "FireplaceQu", mapFireQu)
    df = get_ordinal(df, "GarageFinish", mapGarageFin)
    return df

def get_ordinal(dataframe: DataFrame, column: str, maps):
    # Impute missing values with a specific category (e.g., "NA")
    encoder = OrdinalEncoder(categories=[maps])
    dataframe[column] = encoder.fit_transform(dataframe[[column]])
    return dataframe

def _is_dtype(column):
    return column.dtype == "O"