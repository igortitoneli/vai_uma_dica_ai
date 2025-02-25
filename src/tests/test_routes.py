from random import randint
from uuid import uuid4

from modules.auth.dto.payload.login import LoginPayload
from modules.auth.dto.response.login import LoginResponse
from modules.customers.dto.payload.customers_create import CustomersCreate
from modules.customers.dto.payload.customers_edit import CustomersEdit
from modules.customers.dto.response.cutomers import CustomersResponse
from flask.testing import FlaskClient

from modules.places.dto.payload.places_create import PlacesCreate
from modules.places.dto.payload.places_edit import PlacesEdit
from modules.places.dto.response.places import PlacesResponse
from modules.reviews.dto.payload.reviews_create import ReviewsCreate
from modules.reviews.dto.response.reviews import ReviewsResponse

access_token: str = ""
places_id: int = 0
customers_id: int = 0


def login(client: FlaskClient, payload: LoginPayload):
    response = client.post(
        "/login",
        json=payload.model_dump(),
        headers=client.headers,
    )
    assert response.status_code == 200
    return LoginResponse(**response.get_json())


def test_customers_create(client: FlaskClient):
    payload = CustomersCreate(
        name="test",
        email=f"test_{uuid4().hex}@test.com",
        password="test123",
        phone="123",
    )
    response = client.post(
        "/customers/",
        json=payload.model_dump(),
        headers=client.headers,
    )
    assert response.status_code == 200
    response = CustomersResponse(**response.get_json())

    assert response.name == payload.name
    assert response.email == payload.email
    assert response.phone == payload.phone
    global customers_id
    customers_id = response.id

    login_response = login(
        client,
        LoginPayload(
            email=payload.email,
            password=payload.password,
        ),
    )
    global access_token
    access_token = f"Bearer {login_response.access_token}"


def test_customers_patch(client: FlaskClient):
    payload = CustomersEdit(
        id=customers_id,
        name="test_edited",
        email=f"test_{uuid4().hex}@test.com",
        phone="123",
    )
    global access_token
    response = client.patch(
        "/customers/",
        json=payload.model_dump(),
        headers={
            **client.headers,
            "Authorization": access_token,
        },
    )

    assert response.status_code == 200
    response = CustomersResponse(**response.get_json())

    assert response.name == payload.name
    assert response.email == payload.email
    assert response.phone == payload.phone


def test_places_create(client: FlaskClient):
    payload = PlacesCreate(
        address=f"address_{uuid4().hex}",
        latitude=0.0,
        longitude=0.0,
        name=f"name_{uuid4().hex}",
    )

    global access_token
    response = client.post(
        "/places/",
        json=payload.model_dump(),
        headers={
            **client.headers,
            "Authorization": access_token,
        },
    )

    assert response.status_code == 200
    response = PlacesResponse(**response.get_json())

    assert response.name == payload.name
    assert response.address == payload.address
    assert response.latitude == payload.latitude
    assert response.longitude == payload.longitude
    global places_id
    places_id = response.id


def test_places_patch(client: FlaskClient):
    global places_id
    payload = PlacesEdit(
        id=places_id,
        address=f"address_{uuid4().hex}",
        latitude=0.0,
        longitude=0.0,
        name=f"name_{uuid4().hex}",
    )

    global access_token
    response = client.patch(
        f"/places/{payload.id}",
        json=payload.model_dump(),
        headers={
            **client.headers,
            "Authorization": access_token,
        },
    )

    assert response.status_code == 200
    response = PlacesResponse(**response.get_json())

    assert response.id == payload.id
    assert response.name == payload.name
    assert response.address == payload.address
    assert response.latitude == payload.latitude
    assert response.longitude == payload.longitude


def test_review_create(client: FlaskClient):
    payload = ReviewsCreate(
        places_id=1,
        message=f"message_{uuid4().hex}",
        stars=randint(1, 5),
        customers_id=1,
    )

    global access_token
    response = client.post(
        "/reviews/",
        json=payload.model_dump(),
        headers={
            **client.headers,
            "Authorization": access_token,
        },
    )

    assert response.status_code == 200
    response = ReviewsResponse(**response.get_json())

    assert response.message == payload.message
    assert response.stars == payload.stars
