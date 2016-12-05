# -*- coding: utf-8 -*-
"""The like post Handler."""

import app.helpers as helpers

from post import PostHandler


class LikePostHandler(PostHandler):
    """Like a post."""

    @helpers.user_required
    def get(self, id):
        """like a post.

        Todo:
            * Move in to post method.
        """
        post = self.get_post_by_id(id)

        if post.liked_by(self.user):
            self.flash('You have liked this already.', 'warning')
        elif post.check_author(self.user):
            self.flash('You cannot like your post\'s.', 'error')
        else:
            PostLikes(post_key=post.key, user_key=self.user.key).put()
            self.flash('Thank you for your like.', 'success')
            time.sleep(0.5)

        self.redirect(self.uri_for('post', id=post.key.id(), slug=post.slug))
        return
