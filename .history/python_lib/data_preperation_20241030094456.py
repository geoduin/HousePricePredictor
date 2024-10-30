
def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    
    # Outliers verwijderen, mits het aantal niet te groot is.
    df["GrLivArea"] = df[df["GrLivArea"] < 4000]
    df["OverallQual"] = df[df["OverallQual"] > 1]
    df["TotRmsAbvGrd"] = df[df["TotRmsAbvGrd"] < 11]
    
    return df

def _is_dtype(column):
    return column.dtype == "O"