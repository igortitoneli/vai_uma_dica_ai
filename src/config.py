from dataclasses import dataclass
from datetime import timedelta
import os


@dataclass
class Config:
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ["true", "1"]
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
    token_expires = os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI", "")

    @property
    def JWT_ACCESS_TOKEN_EXPIRES(self):
        return timedelta(hours=int(self.token_expires))
