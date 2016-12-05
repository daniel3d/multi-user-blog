# -*- coding: utf-8 -*-
"""The post Handler."""

import app.helpers as helpers

from app.models import Post
from base import BaseHandler


class PostHandler(BaseHandler):
    """Base controller for posts."""

    @helpers.user_required
    def get(self, id, slug=None):
        """Display existing post."""
        post = self.get_post_by_id(id)

        if not post:
            self.error(404)
            return

        # If no slug redirect to the full slug url...
        if not slug:
            self.redirect(self.uri_for('post', id=int(id), slug=post.slug))

        # Let display the post...
        self.view('post.html', post=post)

    def get_post_by_id(self, post_id):
        """Commonly used function to retrive post by id."""
        return Post.get_by_id(int(post_id))
