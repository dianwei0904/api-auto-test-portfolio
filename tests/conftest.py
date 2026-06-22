import pytest

from api_client import ApiClient
from payloads.booking_payload import valid_booking_payload


BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def api():
    return ApiClient(BASE_URL)


@pytest.fixture(scope="session")
def token(api):
    login_payload = {
        "username": "admin",
        "password": "password123"
    }

    response = api.post("/auth", json=login_payload)

    assert response.status_code == 200
    assert "token" in response.json()

    return response.json()["token"]


@pytest.fixture()
def created_booking(api, token):
    response = api.post("/booking", json=valid_booking_payload())

    assert response.status_code == 200
    assert "bookingid" in response.json()

    booking_id = response.json()["bookingid"]

    yield booking_id

    api.delete(
        f"/booking/{booking_id}",
        headers={"Cookie": f"token={token}"}
    )