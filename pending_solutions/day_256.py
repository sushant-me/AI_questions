import pandas as pd
from surprise import Dataset, Reader, SVD, evaluate

def build_recommendation_system(ratings_file):
    """
    Build recommendation system.
    
    Args:
    ratings_file (str): Path to the ratings file.
    
    Returns:
    pd.DataFrame: DataFrame with user recommendations.
    """
    # Load data
    reader = Reader(line_format='user item rating timestamp', sep=',')
    data = Dataset.load_from_file(ratings_file, reader)
    
    # Train model
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    
    # Generate recommendations
    testset = trainset.build_testset()
    predictions = algo.test(testset)
    
    # Convert predictions to DataFrame
    recommendations = pd.DataFrame(predictions, columns=['user_id', 'item_id', 'true_rating', 'est_rating', 'details'])
    
    return recommendations

# Example usage
ratings_file = 'https://example.com/ratings.csv'
recommendations = build_recommendation_system(ratings_file)
print(recommendations)