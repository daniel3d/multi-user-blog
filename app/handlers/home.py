# -*- coding: utf-8 -*-
"""The home Handler."""

import app.helpers as helpers

from app.models import Post
from base import BaseHandler


class HomeHandler(BaseHandler):
    """Home Handler."""

    @helpers.user_required
    def get(self):
        """Display most reacent posts."""
        posts = Post.query().order(-Post.created_at).fetch(10)
        self.view('home.html', posts=posts)
        return
