import requests
import pytest

BASE_URL = "http://localhost:5000"  # Adjust if your API is hosted on a different port or URL

# Test for adding a Model
def test_add_model():
    payload = {"name": "Test Model", "owner": "Test Owner"}
    response = requests.post(f"{BASE_URL}/model", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

# Test for adding a Model without an owner (intentional failure)
def test_add_model_no_owner():
    payload = {"name": "Test Model No Owner"}
    response = requests.post(f"{BASE_URL}/model", json=payload)
    assert response.status_code == 400  # Expect failure

# Test for getting a Model by ID
def test_get_model():
    response = requests.get(f"{BASE_URL}/model/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Model"

# Test for deleting a Model by ID
def test_delete_model():
    response = requests.delete(f"{BASE_URL}/model/1")
    assert response.status_code == 204

# Test for adding a Model Version
def test_add_model_version():
    payload = {"version": "1.0", "description": "Initial version"}
    response = requests.post(f"{BASE_URL}/model/1/version", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

# Test for inference endpoint
def test_inference():
    payload = {"input_data": "test input"}
    response = requests.post(f"{BASE_URL}/model/1/inference", json=payload)
    assert response.status_code == 200
    assert "output" in response.json()
