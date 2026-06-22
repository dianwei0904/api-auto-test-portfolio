def valid_booking_payload(
    firstname: str = "Nori",
    lastname: str = "Lin",
    totalprice: int = 3000,
    depositpaid: bool = True
):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": "2026-07-01",
            "checkout": "2026-07-03"
        },
        "additionalneeds": "Breakfast"
    }


def updated_booking_payload():
    return {
        "firstname": "Nori",
        "lastname": "Updated",
        "totalprice": 5000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-05"
        },
        "additionalneeds": "Late checkout"
    }