from sklearn.metrics import accuracy_score

def evaluate_model_accuracy(y_true, y_pred):
    """
    Evaluate model accuracy.

    Args:
    y_true (array-like): True labels.
    y_pred (array-like): Predicted labels.

    Returns:
    float: Accuracy score.
    """
    return accuracy_score(y_true, y_pred)