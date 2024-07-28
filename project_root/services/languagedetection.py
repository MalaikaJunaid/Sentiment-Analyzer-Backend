from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

def detect_language(text):
    """
    Detects the language of the given text using langdetect.
    This implementation handles edge cases like short texts or mixed languages.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: The detected language code (e.g., 'en' for English).
    """
    try:
        # Detect the language
        detected_language = detect(text)
        return detected_language
    except LangDetectException:
        # Handle cases where language detection fails
        return "unknown"

def detect_language_with_confidence(text):
    """
    Detects the language of the given text and returns languages with confidence scores.
    Handles short or mixed text cases by returning multiple language possibilities.

    Args:
        text (str): The input text to analyze.

    Returns:
        list: A list of tuples with language codes and confidence scores.
    """
    try:
        # Detect languages with confidence scores
        results = detect_langs(text)
        return [(str(lang.lang), lang.prob) for lang in results]
    except LangDetectException:
        # Handle cases where language detection fails
        return [("unknown", 0.0)]

    # Dummy language detection logic
    # return 'en' if 'hello' in text.lower() else 'unknown'
