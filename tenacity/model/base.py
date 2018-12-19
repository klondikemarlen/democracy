from sqlalchemy.exc import DatabaseError

from tenacity import db

convention = {
  "ix": 'ix_%(column_0_label)s',
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(column_0_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

# I'm not sure if this is valid code?
db.Model.metadata.naming_convention = convention


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Thanks to https://chase-seibert.github.io/blog/2016/03/31/flask-sqlalchemy-sessionless.html
    def save(self):
        db.session.add(self)
        self._flush()
        return self

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def delete(self):
        db.session.delete(self)
        self._flush()

    def _flush(self):
        try:
            db.session.flush()
        except DatabaseError:
            db.session.rollback()
            raise


# Allows direct access the the query from Base.
# Base.query = db.session.query_property()
