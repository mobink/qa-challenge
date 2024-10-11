import requests
import pytest
import uuid

BASE_URL = "http://127.0.0.1:8000"  # Change this to your actual base API URL


@pytest.fixture
def model_id(request):
    new_model = {
        "name": f"Temporary Model {uuid.uuid4()}",
        "owner": "owner_id"
    }
    response = requests.post(f"{BASE_URL}/models", json=new_model)

    if response.status_code != 200:
        pytest.fail(f"Failed to create model: {response.status_code}, {response.json()}")

    model_id_value = response.json()["id"]

    # Add a teardown step to delete the model after tests are done
    def cleanup():
        requests.delete(f"{BASE_URL}/models/{model_id_value}")

    request.addfinalizer(cleanup)  # Ensure the model is deleted after tests

    return model_id_value


def test_get_models():
    response = requests.get(f"{BASE_URL}/models")
    if response.status_code == 200:
        print("Get Models Success:", response.json())
    else:
        print("Get Models Error:", response.status_code, response.json())


def test_add_model():
    new_model = {
        "name": "My New Model",
        "owner": "owner_id"
    }

    response = requests.post(f"{BASE_URL}/models", json=new_model)
    if response.status_code == 200:
        print("Add Model Success:", response.json())
    elif response.status_code == 422:
        print("Add Model Validation Error:", response.json())
    else:
        print("Add Model Error:", response.status_code, response.json())


def test_delete_model(model_id):
    response = requests.delete(f"{BASE_URL}/models/{model_id}")
    if response.status_code == 200:
        print("Delete Model Success")
    elif response.status_code == 422:
        print("Delete Model Validation Error:", response.json())
    else:
        print("Delete Model Error:", response.status_code, response.json())


def test_get_model_versions(model_id):
    response = requests.get(f"{BASE_URL}/models/{model_id}/versions")
    if response.status_code == 200:
        print("Get Model Versions Success:", response.json())
    else:
        print("Get Model Versions Error:", response.status_code, response.json())


def test_add_model_version(model_id):
    new_model_version = {
        "name": "My New Model Version",
        "hugging_face_model": "some-hugging-face-model"
    }

    response = requests.post(f"{BASE_URL}/models/{model_id}/versions", json=new_model_version)
    if response.status_code == 200:
        print("Add Model Version Success:", response.json())
    elif response.status_code == 422:
        print("Add Model Version Validation Error:", response.json())
    else:
        print("Add Model Version Error:", response.status_code, response.json())


# An additional test for adding a different model version
def test_add_model_version_different_case(model_id):
    new_model_version = {
        "name": "Another Model Version",
        "hugging_face_model": "another-hugging-face-model"
    }

    response = requests.post(f"{BASE_URL}/models/{model_id}/versions", json=new_model_version)
    if response.status_code == 200:
        print("Add Model Version Different Case Success:", response.json())
    elif response.status_code == 422:
        print("Add Model Version Different Case Validation Error:", response.json())
    else:
        print("Add Model Version Different Case Error:", response.status_code, response.json())


def run_tests():
    test_get_models()
    test_add_model()
    # Call both version tests here
    if 'model_id' in globals():  # Ensure model_id fixture context is available
        test_add_model_version(model_id)
        test_add_model_version_different_case(model_id)


if __name__ == "__main__":
    run_tests()
