import pandas as pd
import numpy as np
def df_null_percentage(df = None):
    """
    input: DataFrame
    returns: % of Nulls in the dataframe's rows 
    """
    train_missing = (1 - df.count()/len(df)) * 100
    return train_missing.sort_values(ascending = False)


#Date Conversion:
def date_format_conversion(df = None):
    """
    Function converts all the columns having 'Date' in datetimestamp
    """
    date_cols = [col for col in df.columns if 'Date' in col]
    for col in df.columns:
        if col in date_cols:
            df[col] = pd.to_datetime(df[col])
    return df


def valid_age(age:int):
    if age < 0:
        if abs(age) >= 18 and abs(age) < 100:
            return int(abs(age))
    elif age < 18:
        return np.nan
    elif age > 100:
        return np.nan
    else:
        return int(age)