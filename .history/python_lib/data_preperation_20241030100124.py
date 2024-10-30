
def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    

    
    return df

def remove_outliers(df):
    # Outliers verwijderen, mits het aantal niet te groot is.
    filtering_grlivArea = df["GrLivArea"] < 4000
    df["GrLivArea"] = df[filtering_grlivArea]

    filtering_overqual = df["OverallQual"] > 1
    df["OverallQual"] = df[filtering_overqual]

    filtering_totRms = df["TotRmsAbvGrd"] < 11
    df["TotRmsAbvGrd"] = df[filtering_totRms]
    
    return df

def _is_dtype(column):
    return column.dtype == "O"