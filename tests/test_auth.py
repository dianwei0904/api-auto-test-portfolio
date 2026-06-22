import pytest
import allure


@allure.feature("Auth API")
@allure.story("Login")
@pytest.mark.smoke
def test_login_success(api):
    with allure.step("Prepare login payload"):
        payload = {
            "username": "admin",
            "password": "password123"
        }

    with allure.step("Send POST /auth request"):
        response = api.post("/auth", json=payload)

    with allure.step("Verify response status code and token"):
        assert response.status_code == 200
        body = response.json()
        assert "token" in body
        assert body["token"] != ""


@allure.feature("Auth API")
@allure.story("Login failed")
@pytest.mark.negative
def test_login_failed_with_wrong_password(api):
    payload = {
        "username": "admin",
        "password": "wrong_password"
    }

    response = api.post("/auth", json=payload)

    assert response.status_code == 200
    assert response.json()["reason"] == "Bad credentials"