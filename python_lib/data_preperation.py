
def impute_empty_category_data(df):

    # Missende waarden opvullen met NA waarde.
    df["FireplaceQu"] = df["FireplaceQu"].fillna("NA")
    df["GarageFinish"] = df["GarageFinish"].fillna("NA")
    
    return df

def remove_outliers(df):
    # Outliers verwijderen, mits het aantal niet te groot is.
    clean_liv_area_filter = df["GrLivArea"] < 4000
    cleaned_grlive = df[clean_liv_area_filter]
    
    # OverallQuality
    clean_overall_quality_filter = cleaned_grlive["OverallQual"] > 1
    clean_quality = cleaned_grlive[clean_overall_quality_filter]

    # TotRms
    clean_totRms_filter = clean_quality["TotRmsAbvGrd"] < 11
    clean_data = clean_quality[clean_totRms_filter]
    
    return clean_data

def _is_dtype(column):
    return column.dtype == "O"