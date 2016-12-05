# -*- coding: utf-8 -*-
"""The comment post Handler."""

from post import time, user_required, PostComment, PostHandler


class CommentPostHandler(PostHandler):
    """Comment on post."""

    @user_required
    def post(self, id):
        """Add the comment."""
        post = self.get_post_by_id(id)
        comment = self.request.get('comment').strip()
        if comment:
            PostComment(post_key=post.key, user_key=self.user.key,
                        comment=comment).put()
            self.flash('Thank you for your comment.', 'success')
            time.sleep(0.5)
        else:
            self.flash('You cannot submit empty comment', 'error')
        self.redirect(self.uri_for('post', id=post.key.id(), slug=post.slug))
        return
