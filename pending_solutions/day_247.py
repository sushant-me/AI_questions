from collections import Counter
from math import sqrt

def euclidean_distance(point1, point2):
    return sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

def k_nearest_neighbors(data, query_point, k):
    """
    Implement k-nearest neighbors.
    """
    distances = []
    for point, label in data:
        distance = euclidean_distance(point, query_point)
        distances.append((distance, label))
    distances.sort()
    k_nearest = distances[:k]
    labels = [label for _, label in k_nearest]
    return Counter(labels).most_common(1)[0][0]

# Example usage:
data = [([2, 3], 'A'), ([5, 8], 'B'), ([7, 9], 'A'), ([1, 0], 'B')]
query_point = [3, 2]
k = 2
print(k_nearest_neighbors(data, query_point, k))  # Output: 'A'