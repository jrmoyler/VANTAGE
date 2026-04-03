from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json() == {'ok': True}


def test_generate_validation():
    response = client.post('/api/generate', json={'intent': 'short'})
    assert response.status_code == 422


def test_generate_success():
    response = client.post('/api/generate', json={'intent': 'Build a cinematic analytics dashboard with motion and ai tooling'})
    assert response.status_code == 200
    data = response.json()
    assert 'components' in data and len(data['components']) > 4
    assert 'structured_prompt' in data


def test_security_headers_present():
    response = client.get('/api/health')
    assert response.headers['x-content-type-options'] == 'nosniff'
    assert response.headers['x-frame-options'] == 'DENY'
    assert 'content-security-policy' in response.headers


def test_ask_search():
    response = client.post('/api/ask', json={'query': 'kurosawa'})
    assert response.status_code == 200
    payload = response.json()
    assert 'results' in payload
    assert payload['total'] >= 1
