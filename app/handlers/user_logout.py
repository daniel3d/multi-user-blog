# -*- coding: utf-8 -*-
"""The logout user Handler."""

from user import UserHandler


class LogoutUserHandler(UserHandler):
    """Logout page."""

    def get(self):
        """Destroy user sesion."""
        self.auth.unset_session()
        self.redirect(self.uri_for('auth.login'))
