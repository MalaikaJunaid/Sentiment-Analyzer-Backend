from flask import Flask, request, jsonify
from models.sentiment_model import analyze_sentiment, analyze_batch, collect_feedback

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    sentiment = analyze_sentiment(text)
    return jsonify({"sentiment": sentiment})

@app.route('/batch-analyze', methods=['POST'])
def batch_analyze():
    texts = request.json.get('texts')
    if not texts or not isinstance(texts, list):
        return jsonify({"error": "Invalid input"}), 400
    sentiments = analyze_batch(texts)
    return jsonify({"sentiments": sentiments})

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback = request.json.get('feedback')
    if not feedback:
        return jsonify({"error": "No feedback provided"}), 400
    collect_feedback(feedback)
    return jsonify({"message": "Feedback received"}), 200

if __name__ == '__main__':
    app.run(debug=True)
