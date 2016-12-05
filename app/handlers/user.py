# -*- coding: utf-8 -*-
"""The user Handler."""

import app.config as config
import app.helpers as helpers

from base import BaseHandler


class UserHandler(BaseHandler):
    """Base controller for User functionality."""

    def valid_username(self, username):
        """Check if the username is valid."""
        return username and config.REGEXR_USERNAME.match(username)

    def valid_password(self, password):
        """Check if the password is valid."""
        return password and config.REGEXR_PASSWORD.match(password)

    def valid_email(self, email):
        """Check if the email is valid."""
        return not email or config.REGEXR_EMAIL.match(email)
