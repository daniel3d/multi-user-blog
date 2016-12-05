# -*- coding: utf-8 -*-
"""Globaly used functions."""

import hmac

from config import APP_KEY
from webapp2_extras import auth


def make_secure_value(val):
    """Generate secure string."""
    return '%s:%s' % (val, hmac.new(APP_KEY, val).hexdigest())


def check_secure_value(sec):
    """Check if secure string have is not manipulated."""
    val = sec.split(':')[0]
    if sec == make_secure_value(val):
        return val


def user_required(handler):
    """Decorator that checks if there's a user login."""

    def check_login(self, *args, **kwargs):
        """Redirect user too login page if not login."""
        auth = self.auth
        if not auth.get_user_by_session():
            self.redirect(self.uri_for('auth.login'), abort=True)
        else:
            return handler(self, *args, **kwargs)
    return check_login
