# models.py

from google.appengine.ext import db


class Post(db.Model):
    slug = db.StringProperty(required = True)
    title = db.StringProperty(required = True)
    ribbon = db.StringProperty()
    content = db.TextProperty(required = True)
    markdown = db.TextProperty(required = True)
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)