class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        if depth == self.max_depth or len(set(y)) == 1:
            return {"prediction": self._majority_vote(y)}
        
        best_feature, best_threshold = self._find_best_split(X, y)
        if best_feature is None:
            return {"prediction": self._majority_vote(y)}
        
        left_mask = X[:, best_feature] < best_threshold
        right_mask = X[:, best_feature] >= best_threshold
        
        left_tree = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right_tree = self._build_tree(X[right_mask], y[right_mask], depth + 1)
        
        return {
            "feature": best_feature,
            "threshold": best_threshold,
            "left": left_tree,
            "right": right_tree
        }

    def predict(self, X):
        return [self._predict_single(x) for x in X]

    def _predict_single(self, x):
        node = self.tree
        while "prediction" not in node:
            feature = node["feature"]
            threshold = node["threshold"]
            if x[feature] < threshold:
                node = node["left"]
            else:
                node = node["right"]
        return node["prediction"]

    def _majority_vote(self, y):
        return max(set(y), key=y.count)

    def _find_best_split(self, X, y):
        best_feature = None
        best_threshold = None
        best_gain = 0
        
        for feature in range(X.shape[1]):
            thresholds = sorted(set(X[:, feature]))
            for i in range(1, len(thresholds)):
                threshold = (thresholds[i - 1] + thresholds[i]) / 2
                gain = self._information_gain(y, feature, threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold
        
        return best_feature, best_threshold

    def _information_gain(self, y, feature, threshold):
        parent_entropy = self._entropy(y)
        
        left_mask = y[X[:, feature] < threshold]
        right_mask = y[X[:, feature] >= threshold]
        
        left_entropy = self._entropy(left_mask)
        right_entropy = self._entropy(right_mask)
        
        weight_left = len(left_mask) / len(y)
        weight_right = len(right_mask) / len(y)
        
        gain = parent_entropy - (weight_left * left_entropy + weight_right * right_entropy)
        return gain

    def _entropy(self, y):
        from collections import Counter
        counts = Counter(y)
        total = len(y)
        entropy = 0
        for count in counts.values():
            probability = count / total
            entropy -= probability * self._log2(probability)
        return entropy

    def _log2(self, x):
        import math
        return math.log2(x) if x > 0 else 0