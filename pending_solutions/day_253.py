from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_email_data():
    # Placeholder for loading email data
    # This should return a tuple (texts, labels)
    # texts is a list of email texts
    # labels is a list of labels (0 for ham, 1 for spam)
    pass

def build_spam_classifier():
    """ Build spam email classifier. """
    texts, labels = load_email_data()
    
    # Split data into training and testing sets
    texts_train, texts_test, labels_train, labels_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42
    )
    
    # Create a pipeline with CountVectorizer and MultinomialNB
    classifier = make_pipeline(CountVectorizer(), MultinomialNB())
    
    # Train the classifier
    classifier.fit(texts_train, labels_train)
    
    # Make predictions
    predictions = classifier.predict(texts_test)
    
    # Evaluate the classifier
    accuracy = accuracy_score(labels_test, predictions)
    print(f"Classifier accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    build_spam_classifier()