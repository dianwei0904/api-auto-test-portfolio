import pytest
import allure

from payloads.booking_payload import valid_booking_payload, updated_booking_payload


@allure.feature("Booking API")
@allure.story("Create booking")
@pytest.mark.smoke
def test_create_booking(api):
    payload = valid_booking_payload()

    response = api.post("/booking", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == payload["firstname"]
    assert body["booking"]["lastname"] == payload["lastname"]
    assert body["booking"]["totalprice"] == payload["totalprice"]


@allure.feature("Booking API")
@allure.story("Get booking")
@pytest.mark.smoke
def test_get_created_booking(api, created_booking):
    booking_id = created_booking

    response = api.get(f"/booking/{booking_id}")

    assert response.status_code == 200

    body = response.json()
    assert body["firstname"] == "Nori"
    assert body["lastname"] == "Lin"
    assert body["totalprice"] == 3000


@allure.feature("Booking API")
@allure.story("Update booking")
@pytest.mark.smoke
def test_update_booking(api, token, created_booking):
    booking_id = created_booking
    payload = updated_booking_payload()

    response = api.put(
        f"/booking/{booking_id}",
        json=payload,
        headers={"Cookie": f"token={token}"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["lastname"] == "Updated"
    assert body["totalprice"] == 5000
    assert body["additionalneeds"] == "Late checkout"


@allure.feature("Booking API")
@allure.story("Delete booking")
@pytest.mark.smoke
def test_delete_booking(api, token):
    create_response = api.post("/booking", json=valid_booking_payload())
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    delete_response = api.delete(
        f"/booking/{booking_id}",
        headers={"Cookie": f"token={token}"}
    )

    assert delete_response.status_code == 201

    get_response = api.get(f"/booking/{booking_id}")
    assert get_response.status_code == 404