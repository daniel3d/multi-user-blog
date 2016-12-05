# -*- coding: utf-8 -*-
"""The home Handler."""

from base import user_required, BaseHandler
from app.models import Post


class BlogHandler(BaseHandler):
    """Home Handler."""

    @user_required
    def get(self):
        """Display most reacent posts."""
        posts = Post.query().order(-Post.created_at).fetch(10)
        self.view('home.html', posts=posts)
        return
