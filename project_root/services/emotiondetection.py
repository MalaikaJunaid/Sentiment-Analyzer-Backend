from transformers import pipeline
# Load an emotion classification pipeline with a pre-trained model
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def detect_emotion(text):
    try:
        # Analyze the text to get a list of emotion predictions
        results = emotion_pipeline(text, return_all_scores=True)

        # Extract scores and labels
        emotions = results[0]
        emotion_scores = {emotion['label']: emotion['score'] for emotion in emotions}

        # Find the emotion with the highest score
        max_emotion = max(emotion_scores, key=emotion_scores.get)

        # Handle edge cases
        if max_emotion == "neutral" or emotion_scores[max_emotion] < 0.5:
            return "neutral"
        return max_emotion
    except Exception as e:
        print(f"Error detecting emotion: {e}")
        return "unknown"
        
    # Dummy emotion detection logic
    # return 'happy' if 'happy' in text.lower() else 'neutral'
