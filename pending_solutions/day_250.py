"""
Normalize dataset.
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_dataset(data):
    """
    Normalize the dataset using MinMaxScaler.
    
    Args:
    data (pd.DataFrame): The dataset to be normalized.
    
    Returns:
    pd.DataFrame: The normalized dataset.
    """
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    return pd.DataFrame(normalized_data, columns=data.columns)

# Example usage
# df = pd.read_csv('https://example.com/dataset.csv')
# normalized_df = normalize_dataset(df)