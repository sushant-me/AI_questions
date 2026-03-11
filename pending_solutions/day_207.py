import pandas as pd

# Use Pandas to create DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
}

df = pd.DataFrame(data)
print(df)