# coding: utf-8
"""The Post models."""

import random
import app.config as config

from post_likes import PostLike
from post_comments import PostComment
from google.appengine.ext import ndb


class Post(ndb.Model):
    """Posts db model."""

    user_key = ndb.KeyProperty(kind='User')
    slug = ndb.StringProperty()
    ribbon = ndb.StringProperty()
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    markdown = ndb.TextProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    @property
    def post_likes(self):
        """Get all likes for tis post."""
        return PostLike.query().filter(PostLike.post_key == self.key)

    @property
    def post_comments(self):
        """Get all comments for tis post."""
        return PostComment.query().order(-PostComment.created_at).filter(
            PostComment.post_key == self.key)

    @property
    def user(self):
        """Get the user for this post by using the stored key."""
        return self.user_key.get()

    def get_ribbon_style(self):
        """Get ribbon style url or colour."""
        if not self.ribbon:
            self.ribbon = random.choice(config.COLOR_PALETTE)
            self.put()

        if self.ribbon[:1] == '#':
            return 'style="background: %s;"' % self.ribbon
        else:
            return 'style="background: url(%s) center / cover;"' % self.ribbon

    def check_author(self, u):
        """Check if given user is the author of the post."""
        return u.key == self.user_key

    def liked_by(self, u):
        """Check if given user already liked the post."""
        return PostLike.query().filter(PostLike.post_key == self.key,
                                       PostLike.user_key == u.key).fetch()
