import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Hello, World!"
    assert data['version'] == "1.0"
    assert data['status'] == "success"

def test_info_endpoint(client):
    """Test the info endpoint."""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app_name'] == "Flask Matrix Calculator"
    assert len(data['endpoints']) == 4

def test_health_endpoint(client):
    """Test the health endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"
    assert data['uptime'] == "running"

def test_multiply_endpoint(client):
    """Test the multiply endpoint."""
    response = client.get('/api/multiply/2/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['operand1'] == 2
    assert data['operand2'] == 3
    assert data['result'] == 6
    assert data['operation'] == "multiply"

def test_multiply_zero(client):
    """Test the multiply endpoint with zero."""
    response = client.get('/api/multiply/0/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 0
    
def test_multiply_large_numbers(client):
    """Test the multiply endpoint with large numbers."""
    response = client.get('/api/multiply/1000000/1000000')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 1000000000000
    assert data['operation'] == "multiply"
    