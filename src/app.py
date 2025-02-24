from typing import Any, Mapping, Optional

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from common.exceptions.api_exception import APIException, api_exception_handler
from common.exceptions.not_found_exception import (
    NotFoundException,
    not_found_exception_handler,
)
from common.exceptions.unauthorized_exception import (
    UnauthorizedException,
    unauthorized_exception_handler,
)
from config import Config


def config_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    app = Flask(__name__)
    CORS(
        app,
        resources={
            r"/*": {"origins": "*"},
        },
    )
    app.config.from_object(Config)

    if test_config is not None:
        app.config.from_mapping(test_config)

    return app


def init_db(app: Flask):
    from common.database import db

    try:
        db.init_app(app)
    except Exception as e:
        app.logger.critical(str(e))


def set_blueprints(app: Flask):
    from modules.auth import auth_router
    from modules.customers import customers_router
    from modules.places import places_router
    from modules.reviews import reviews_router

    app.register_blueprint(auth_router.bp)
    app.register_blueprint(customers_router.bp)
    app.register_blueprint(places_router.bp)
    app.register_blueprint(reviews_router.bp)


def register_handlers(app: Flask):
    app.register_error_handler(APIException, api_exception_handler)
    app.register_error_handler(NotFoundException, not_found_exception_handler)
    app.register_error_handler(UnauthorizedException, unauthorized_exception_handler)


def config_jwt(app: Flask):
    JWTManager(app)


def create_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    app = config_app(test_config)
    init_db(app)
    set_blueprints(app)
    register_handlers(app)
    config_jwt(app)

    return app
