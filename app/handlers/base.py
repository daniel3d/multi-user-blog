# -*- coding: utf-8 -*-
"""The base Handler all the handlers extend from this."""

import os
import jinja2
import webapp2
import app.helpers as helpers

from app.models import User
from webapp2_extras import auth
from webapp2_extras import sessions


viewer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(
    os.path.dirname(__file__), '..', 'views')), autoescape=True)
"""Jinja2 template viwer that we can use in our controllers."""


class BaseHandler(webapp2.RequestHandler):
    """Base Controller functionality we need to reuse."""

    @webapp2.cached_property
    def auth(self):
        """Shortcut to access the auth instance as a property."""
        return auth.get_auth()

    @webapp2.cached_property
    def user_info(self):
        """Shortcut to access a subset of the user attributes that are stored.

        in the session.
        The list of attributes to store in the session is specified in
          config['webapp2_extras.auth']['user_attributes'].
        :returns
          A dictionary with most user information
        """
        return self.auth.get_user_by_session()

    @webapp2.cached_property
    def user(self):
        """Shortcut to access the current logged in user.

        Unlike user_info, it fetches information from the persistence layer and
        returns an instance of the underlying model.
        :returns
            The instance of the user model associated to the logged in user.
        """
        u = self.user_info
        return User.get_by_id(u['user_id']) if u else None

    def write(self, *a, **kw):
        """Send response to the browser."""
        self.response.out.write(*a, **kw)

    def view(self, template, **params):
        """Render template with given varibles."""
        view = viewer.get_template(template)
        self.write(view.render(
            params, messages=self.flash_messages, curent_user=self.user,
            version=config.VERSION))

    def dispatch(self):
        """Get a session store for this request."""
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        """Return a session using the default cookie key."""
        return self.session_store.get_session()

    @webapp2.cached_property
    def flash_messages(self):
        """Implement flash messages."""
        return self.session.get_flashes(key='_messages')

    def flash(self, message, level='warning'):
        """Flash message."""
        self.session.add_flash(message, level, key='_messages')

    def set_secure_cookie(self, name, val):
        """Set secure cookie."""
        cookie_val = helpers.make_secure_value(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        """Read secure cookie."""
        cookie_val = self.request.cookies.get(name)
        return cookie_val and helpers.check_secure_value(cookie_val)
