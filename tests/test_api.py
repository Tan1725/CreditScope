"""
test_api.py - Integration and unit tests for FastAPI endpoints
"""

import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health_check_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"


def test_predict_invalid_payload_returns_422(client):
    # Missing required loan application fields
    response = client.post("/predict", json={})
    assert response.status_code == 422
