import datetime


class TokenConfig:
    def __init__(
        self,
        token_expiration: datetime.timedelta = datetime.timedelta(hours=24),
        fresh_token_expiration: datetime.timedelta = datetime.timedelta(minutes=10),
    ):

        self.token_expiration = token_expiration
        self.fresh_token_expiration = fresh_token_expiration
