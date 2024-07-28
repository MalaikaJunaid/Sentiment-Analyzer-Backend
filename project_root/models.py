from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    records = db.relationship('AnalysisRecord', backref='user', lazy=True)

class AnalysisRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    emotion = db.Column(db.String(20), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
