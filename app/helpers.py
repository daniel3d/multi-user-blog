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
