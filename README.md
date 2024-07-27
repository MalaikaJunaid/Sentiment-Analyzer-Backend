# Text Sentiment Analyzer

This project is a Flask-based API for performing sentiment analysis on text using Hugging Face's transformers library.

## Setup

   1. Clone the repository:
      ```bash
      git clone https://github.com/yourusername/sentiment-analyzer.git
      cd sentiment-analyzer
      
   2. Install dependencies:
     ```bash
     pip install -r requirements.txt
   
   3. Run the application:
     ```bash
    python app.py

## Endpoints

- `/analyze`: Analyzes a single text for sentiment.
- `/batch-analyze`: Analyzes multiple texts for sentiment.
- `/feedback`: Collects user feedback.

## Testing

Run the tests using:
  ```bash
  pytest
