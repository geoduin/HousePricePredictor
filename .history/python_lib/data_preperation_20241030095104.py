
def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    
    # Outliers verwijderen, mits het aantal niet te groot is.
    grliv = df["GrLivArea"]
    overallQual = df["OverallQual"]
    totRms = df["TotRmsAbvGrd"]

    filtering_grlivArea = grliv < 4000
    filtering_overqual = overallQual > 1
    filtering_totRms = totRms < 11

    # Filter outliers
    df["GrLivArea"] = df[filtering_grlivArea]
    df["OverallQual"] = df[filtering_overqual]
    df["TotRmsAbvGrd"] = df[filtering_totRms]
    
    return df

def _is_dtype(column):
    return column.dtype == "O"