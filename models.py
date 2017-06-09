from ShortUrl import db


class Url(db.Model):
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    origin_url = db.Column(db.String())
    shurl = db.Column(db.String(7), unique=True)

    # __tablename__ = 'url'

    def __init__(self, origin_url, shurl):
        self.origin_url = origin_url
        self.shurl = shurl

    def __repr__(self):
        return '<Url %r>' % self.id
