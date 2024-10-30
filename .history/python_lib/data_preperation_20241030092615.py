
def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    # Outliers verwijderen, mits het aantal niet te groot is.
    
    return df

def _is_dtype(column):
    return column.dtype == "O"