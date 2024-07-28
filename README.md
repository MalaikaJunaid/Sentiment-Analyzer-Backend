# Sentiment Analyzer Backend

This project is a backend service for a sentiment analyzer web application. It includes features like emotion detection, language detection, and sentiment analysis, with user authentication and data management capabilities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Features

- **User Authentication**: Sign up and log in functionality to manage user sessions.
- **Sentiment Analysis**: Analyze text and determine the sentiment as positive or negative.
- **Emotion Detection**: Identify emotions from the input text.
- **Language Detection**: Determine the language of the input text.
- **Data Visualization**: View analysis results with graphical representations.

## Installation

### Prerequisites

- Python 3.8+
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) or [pipenv](https://pipenv.pypa.io/en/latest/)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/sentiment-analyzer-backend.git
   cd sentiment-analyzer-backend
      
2. **Set Up Virtual Environment**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows use          
     `venv\Scripts\activate`

3. **Install Dependencies**:
     ```bash
     pip install -r requirements.txt

4. **Set Up Database**:
     ```bash
     python database.py
     
5. **Run the application**:
     ```bash
    python app.py

## Endpoints

- `POST /signup`: Create a new user account.
- `POST /login`: Authenticate a user.
- `POST /analyze`: Analyze sentiment of text.
- `POST /detect-emotion`: Detect emotion in text.
- `POST /detect-language`: Detect language of text.
- `GET /user/history`: Retrieve the user's analysis history.
  
## Technologies Used
- **Flask**: Web framework for Python.
- **Dask**: Parallel computing with task scheduling.
- **Transformers**: Pre-trained models for natural language processing.
- **SQLite**: Lightweight database for storing user and analysis data.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
