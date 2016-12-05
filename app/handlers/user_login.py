# -*- coding: utf-8 -*-
"""The user Handler."""

import app.config as config
import app.helpers as helpers

from user import UserHandler


class LoginUserHandler(UserHandler):
    """Login page."""

    def get(self):
        """Show login form."""
        self.view('login.html')

    def post(self):
        """Try to login the user."""
        username = self.request.get('username')
        password = self.request.get('password')
        try:
            u = self.auth.get_user_by_password(
                username, password, remember=True, save_session=True)
            self.redirect(self.uri_for('blog'))
        except (InvalidAuthIdError, InvalidPasswordError) as e:
            self.flash('Login failed for user %s because of %s' %
                       (username, type(e)), 'error')
            self.redirect(self.uri_for('auth.login'))