
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