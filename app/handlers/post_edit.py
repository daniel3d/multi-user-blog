# -*- coding: utf-8 -*-
"""The edit post Handler."""

from post import user_required, slugify, PostHandler


class EditPostHandler(PostHandler):
    """Update existing post."""

    @user_required
    def get(self, id):
        """Open edit form for the the post."""
        post = self.get_post_by_id(id)

        if not post:
            self.error(404)
            return

        if post.check_author(self.user):
            self.view('post.edit.html', post=post)
            return
        else:
            self.flash('You cannot edit post: %s' % post.title, 'error')
            self.redirect(self.uri_for('blog'))
            return

    @user_required
    def post(self, id):
        """Submit the eddited post."""
        post = self.get_post_by_id(id)

        if not post:
            self.error(404)
            return

        if post.check_author(self.user):
            post.title = self.request.get('title').strip()
            post.slug = slugify(post.title).strip()
            post.ribbon = self.request.get('ribbon').strip()
            post.markdown = self.request.get('markdown').strip()
            post.content = self.request.get('content').strip()
            post.put()
            self.flash('Well done my friend! Post: %s was Updated.'
                       % (post.title), 'success')
        else:
            self.flash('You cannot edit post: %s' % post.title, 'error')

        self.redirect(self.uri_for('post', id=post.key.id(), slug=post.slug))
        return
