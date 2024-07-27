import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_analyze(client):
    response = client.post('/analyze', json={'text': 'I love this!'})
    assert response.status_code == 200
    assert response.json['sentiment'] == 'POSITIVE'

def test_batch_analyze(client):
    response = client.post('/batch-analyze', json={'texts': ['I love this!', 'I hate this!']})
    assert response.status_code == 200
    assert response.json['sentiments'] == ['POSITIVE', 'NEGATIVE']

def test_feedback(client):
    response = client.post('/feedback', json={'feedback': 'Great tool!'})
    assert response.status_code == 200
    assert response.json['message'] == 'Feedback received'
