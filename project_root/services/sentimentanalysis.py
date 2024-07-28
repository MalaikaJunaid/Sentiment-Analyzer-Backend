import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def preprocess(text):
    return tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

def predict_sentiment(text):
    inputs = preprocess(text)
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    label = torch.argmax(predictions, dim=1).item()
    score = predictions[0][label].item()
    return label, score

def get_sentiment_label(label_id):
    return "POSITIVE" if label_id == 1 else "NEGATIVE"

def analyze_sentiment(text):
    label_id, score = predict_sentiment(text)
    sentiment_label = get_sentiment_label(label_id)
    return sentiment_label, score

def batch_analyze_sentiment(texts):
    results = []
    for text in texts:
        sentiment, confidence = analyze_sentiment(text)
        emotion = detect_emotion(text)
        language = detect_language(text)
        results.append({'text': text, 'sentiment': sentiment, 'confidence': confidence, 'emotion': emotion, 'language': language})
    return results
