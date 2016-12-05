# -*- coding: utf-8 -*-
"""The user Handler."""

import app.config as config
import app.helpers as helpers

from user import UserHandler


class LogoutUserHandler(UserHandler):
    """Logout page."""

    def get(self):
        """Destroy user sesion."""
        self.auth.unset_session()
        self.redirect(self.uri_for('auth.login'))
