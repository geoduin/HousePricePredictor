
def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    
    return df

def remove_outliers(df):
    # Outliers verwijderen, mits het aantal niet te groot is.
    df[
        (df['GrLivArea'] < 4000) &
        (df['OverallQual'] > 1) &
        (df['TotRmsAbvGrd'] < 11) &
        (df['GarageCars'] < 4)
    ]

def _is_dtype(column):
    return column.dtype == "O"