from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from utils.auth_middleware import basic_authentication
from utils.log_middleware import log_request
from services.sentimentanalysis import analyze_sentiment, batch_analyze_sentiment
from services.emotiondetection import detect_emotion
from services.languagedetection import detect_language

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production
db = SQLAlchemy(app)
jwt = JWTManager(app)

from models import User, AnalysisRecord

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = generate_password_hash(data.get('password'), method='sha256')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already registered'}), 409

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/analyze', methods=['POST'])
@jwt_required()
@log_request
def analyze():
    data = request.json
    text = data.get('text')
    sentiment, confidence = analyze_sentiment(text)
    emotion = detect_emotion(text)
    language = detect_language(text)

    user_id = get_jwt_identity()
    record = AnalysisRecord(user_id=user_id, text=text, sentiment=sentiment, emotion=emotion, language=language, confidence=confidence)
    db.session.add(record)
    db.session.commit()

    return jsonify({
        'text': text,
        'sentiment': sentiment,
        'confidence': confidence,
        'emotion': emotion,
        'language': language
    }), 200

@app.route('/batch-analyze', methods=['POST'])
@jwt_required()
@log_request
def batch_analyze():
    data = request.json
    texts = data.get('texts', [])
    results = batch_analyze_sentiment(texts)

    user_id = get_jwt_identity()
    for result in results:
        record = AnalysisRecord(user_id=user_id, **result)
        db.session.add(record)

    db.session.commit()

    return jsonify(results), 200

@app.route('/records', methods=['GET'])
@jwt_required()
def get_records():
    user_id = get_jwt_identity()
    records = AnalysisRecord.query.filter_by(user_id=user_id).all()
    records_data = [{'text': r.text, 'sentiment': r.sentiment, 'emotion': r.emotion, 'language': r.language, 'confidence': r.confidence} for r in records]

    return jsonify(records_data), 200

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
