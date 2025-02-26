import pytest
from app import create_app


@pytest.fixture
def client():
    test_config = {
        "JWT_ACCESS_TOKEN_EXPIRES": 24,
        "JWT_SECRET_KEY": "2ff4dc3f8058c8857f719254ff92a024f3082c46566c4a1603d1285d212faeb42110342b9fc420cbb800dc67364314cd737a740f8141482f114a9d4243acb120246d13a767d5c867e3ace1e8c172e051777e1eb785e5ba6dbd2e0156a5709c9939eedc6b16bda81376270d7b9c93d394dc86b6f8edb4c3f01117c0c958b91b60182fa4970d2cec94bc58695bc079efedbe344a1c8566e3bc4426f42485d2dc9184b9cc11894e5f5b2fddc98b6b78e13aa589cad7c9187a3a911671f8be4ba0ec2acb58fafe0ad7c928bb3f954d6fc3823a94748b1ebb45211692c717a216d8a30b4d638f71b545f7f2e1ffb7b028b01fd7f5e3df45c9d7ad8003bbda0ddae82f",
        "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://user:root@localhost:50001/api?charset=utf8mb4",
        "TESTING": True,
        "DEBUG": "true",
    }
    app = create_app(test_config)

    with app.test_client() as client:
        client.headers = {
            "Content-Type": "application/json",
        }

        yield client
