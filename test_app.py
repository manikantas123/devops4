# app/test_app.py

from app import app

def test_home():
    # Use Flask's test client to simulate requests
    client = app.test_client()
    response = client.get('/')
    
    # Assert the response is OK
    assert response.status_code == 200

    # Assert the response contains the expected text
    assert b"Hello, DevOps World!" in response.data
