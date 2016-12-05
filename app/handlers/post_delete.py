# -*- coding: utf-8 -*-
"""The delete post Handler."""

from post import time, user_required, PostHandler


class DeletePostHandler(PostHandler):
    """Delete existing post."""

    @user_required
    def get(self, id):
        """delete a post.

        Todo:
            * Move in to post method.
        """
        post = self.get_post_by_id(id)

        if post.check_author(self.user):
            post.key.delete()
            self.flash('Post: %s was Deleted.' % post.title, 'warning')
            time.sleep(0.5)
        else:
            self.flash('You cannot delete post: %s' % post.title, 'error')

        self.redirect(self.uri_for('blog'))
        return
