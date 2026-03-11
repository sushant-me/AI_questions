import requests
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        return self.sentiment_pipeline(text)[0]['label']

# Example usage
analyzer = SentimentAnalyzer()
text = "I love this product!"
sentiment = analyzer.analyze_sentiment(text)
print(f"The sentiment of the text is: {sentiment}")