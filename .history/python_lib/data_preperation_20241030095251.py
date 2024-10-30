
def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    
    # Outliers verwijderen, mits het aantal niet te groot is.
    filtering_grlivArea = df["GrLivArea"] < 4000
    filtering_overqual = df["OverallQual"] > 1
    filtering_totRms = df["TotRmsAbvGrd"] < 11

    # Filter outliers
    df["GrLivArea"] = df[filtering_grlivArea]
    df["OverallQual"] = df[filtering_overqual]
    df["TotRmsAbvGrd"] = df[filtering_totRms]
    
    return df

def _is_dtype(column):
    return column.dtype == "O"