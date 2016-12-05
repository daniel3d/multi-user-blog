# coding: utf-8
"""The Post Like model."""

from google.appengine.ext import ndb


class PostLike(ndb.Model):
    """Post Likes db model."""

    user_key = ndb.KeyProperty(kind='User')
    post_key = ndb.KeyProperty(kind='Post')
    created_at = ndb.DateTimeProperty(auto_now_add=True)

    @property
    def user(self):
        """Get the user for this like by using the stored key."""
        return self.user_key.get()
