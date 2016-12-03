# coding: utf-8
"""The app models."""

import webapp2_extras.appengine.auth.models

from google.appengine.ext import ndb

from webapp2_extras import security

from support import time, db, random, config


class User(webapp2_extras.appengine.auth.models.User):
    """Users db model."""

    def set_password(self, raw_password):
        """Set the password for the current user.

        :param raw_password:
            The raw password which will be hashed and stored
        """
        self.password = security.generate_password_hash(
            raw_password, length=12)

    @classmethod
    def get_by_auth_token(cls, user_id, token, subject='auth'):
        """Return a user object based on a user ID and token.

        :param user_id:
            The user_id of the requesting user.
        :param token:
            The token string to be verified.
        :returns:
            A tuple ``(User, timestamp)``, with a user object and
            the token timestamp, or ``(None, None)`` if both were not found.
        """
        token_key = cls.token_model.get_key(user_id, subject, token)
        user_key = ndb.Key(cls, user_id)
        # Use get_multi() to save a RPC call.
        valid_token, user = ndb.get_multi([token_key, user_key])
        if valid_token and user:
            timestamp = int(time.mktime(valid_token.created.timetuple()))
            return user, timestamp

        return None, None


class Post(ndb.Model):
    """Posts db model."""

    user = ndb.StructuredProperty(User)
    slug = ndb.StringProperty()
    ribbon = ndb.StringProperty()
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    markdown = ndb.TextProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    def get_ribbon_style(self):
        """Get ribbon style url or colour."""
        if not self.ribbon:
            self.ribbon = random.choice(config.COLOR_PALETTE)
            self.put()

        if self.ribbon[:1] == '#':
            return 'style="background: %s;"' % self.ribbon
        else:
            return 'style="background: url(%s) center / cover;"' % self.ribbon
