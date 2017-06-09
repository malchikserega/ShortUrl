from ShortUrl import db
from models import *


def add_url(origin_url, shurl):
    try:
        new = Url(origin_url, shurl)
        db.session.add(new)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def get_url(shurl):
    res = Url.query.filter(Url.shurl == shurl).first()
    if res is not None:
        return res.origin_url
    return False
