# coding: utf-8
"""The Post Comment model."""

from google.appengine.ext import ndb


class PostComment(ndb.Model):
    """Post Comments db model."""

    user_key = ndb.KeyProperty(kind='User')
    post_key = ndb.KeyProperty(kind='Post')
    comment = ndb.StringProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)

    @property
    def user(self):
        """Get the user for this comment by using the stored key."""
        return self.user_key.get()
