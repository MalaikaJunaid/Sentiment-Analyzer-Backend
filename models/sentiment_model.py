from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]['label']

def analyze_batch(texts):
    results = sentiment_pipeline(texts)
    return [result['label'] for result in results]

def collect_feedback(feedback):
    # Here you can implement logic to store feedback in a database or a file
    # For simplicity, we'll just print the feedback
    print(f"Feedback received: {feedback}")
