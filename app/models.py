# models.py

from google.appengine.ext import db


class Post(db.Model):
    slug = db.StringProperty()
    title = db.StringProperty()
    ribbon = db.StringProperty()
    content = db.TextProperty()
    markdown = db.TextProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)