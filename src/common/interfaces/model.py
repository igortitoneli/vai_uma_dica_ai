from common.database import db
from common.date_mixin import DateMixin
from common.utils import datetime_now


class Model(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        if isinstance(self, DateMixin):
            self.updated_at = datetime_now()
        db.session.commit()

    def delete(self):
        if isinstance(self, DateMixin):
            self.deleted_at = datetime_now()
        db.session.commit()
