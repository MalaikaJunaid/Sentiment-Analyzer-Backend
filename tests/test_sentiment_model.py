from models.sentiment_model import analyze_sentiment, analyze_batch

def test_analyze_sentiment():
    assert analyze_sentiment('I love this!') == 'POSITIVE'
    assert analyze_sentiment('I hate this!') == 'NEGATIVE'

def test_analyze_batch():
    texts = ['I love this!', 'I hate this!']
    results = analyze_batch(texts)
    assert results == ['POSITIVE', 'NEGATIVE']
