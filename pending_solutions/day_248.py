"""
Perform data preprocessing.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    # Load data
    data = pd.read_csv(file_path)

    # Handle missing values
    data.fillna(data.mean(), inplace=True)

    # Encode categorical variables
    data = pd.get_dummies(data)

    # Normalize numerical variables
    scaler = StandardScaler()
    data[['age', 'income']] = scaler.fit_transform(data[['age', 'income']])

    return data

# Example usage
preprocessed_data = preprocess_data('https://example.com/data.csv')