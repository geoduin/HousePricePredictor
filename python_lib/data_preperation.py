
def impute_empty_category_data(df):
    # Per column impute the column, als het aantal na waarden kolom > 0 is.

    # Als dat het geval is, controleer het datatype.

    # Als het een int64 type is, impute volgens de mean waarde. Tenzij het ordinaal of nominaal is.

    # Als het een Object is, impute NA in. Tenzij anders beschreven.
    
    return df

def _is_dtype(column):
    return column.dtype == "O"