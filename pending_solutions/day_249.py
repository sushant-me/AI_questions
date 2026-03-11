""" Handle missing data. """

import pandas as pd

def handle_missing_data(data):
    """
    Handle missing data in a DataFrame.
    
    Args:
        data (pd.DataFrame): DataFrame containing data with missing values.
    
    Returns:
        pd.DataFrame: DataFrame with missing data handled.
    """
    # Fill missing values with the mean of the column
    data.fillna(data.mean(), inplace=True)
    return data