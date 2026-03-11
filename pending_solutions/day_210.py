"""
Group data using groupby().
"""

from itertools import groupby

data = [('apple', 1), ('banana', 2), ('apple', 3), ('banana', 4), ('cherry', 5)]

# Sort data by the key to ensure groupby works correctly
data.sort(key=lambda x: x[0])

grouped_data = {key: list(group) for key, group in groupby(data, key=lambda x: x[0])}

print(grouped_data)