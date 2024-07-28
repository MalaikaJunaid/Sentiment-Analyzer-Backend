import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def preprocess(text):
    # Tokenize input text
    return tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

def predict_sentiment(text):
    # Preprocess the text
    inputs = preprocess(text)
    
    # Handle cases where text might be empty or just whitespace
    if inputs['input_ids'].size(1) == 0:
        return None, 0.0

    # Perform model inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get predictions
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    label = torch.argmax(predictions, dim=1).item()
    score = predictions[0][label].item()

    return label, score

def get_sentiment_label(label_id):
    # Map label id to sentiment label
    return "POSITIVE" if label_id == 1 else "NEGATIVE"

def analyze_sentiment(text):
    label_id, score = predict_sentiment(text)
    if label_id is None:
        return "NEUTRAL", 0.0  # Default for empty inputs or issues
    sentiment_label = get_sentiment_label(label_id)
    return sentiment_label, score

def batch_analyze_sentiment(texts):
    results = []
    for text in texts:
        # Analyze sentiment
        sentiment, confidence = analyze_sentiment(text)
        emotion = detect_emotion(text)  # Assuming detect_emotion is defined elsewhere
        language = detect_language(text)  # Assuming detect_language is defined elsewhere

        # Append results, include checks to ensure all parts work
        results.append({
            'text': text,
            'sentiment': sentiment,
            'confidence': confidence,
            'emotion': emotion,
            'language': language
        })
    return results
