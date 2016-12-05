# -*- coding: utf-8 -*-
"""The new post Handler."""

from post import user_required, slugify, Post, PostHandler


class NewPostHandler(PostHandler):
    """Create new post."""

    @user_required
    def get(self):
        """Get the new post form."""
        self.view('post.edit.html', post=())
        return

    @user_required
    def post(self):
        """Save new Post to the database."""
        p = {
            "title": self.request.get('title').strip(),
            "slug": slugify(self.request.get('title')),
            "ribbon": self.request.get('ribbon'),
            "markdown": self.request.get('markdown').strip(),
            "content": self.request.get('content').strip()
        }

        try:  # Try saving the post
            post = Post(ribbon=p["ribbon"], markdown=p["markdown"],
                        user_key=self.user.key, title=p["title"],
                        content=p["content"],
                        slug=p["slug"])
            post.put()
        except Exception, error:
            self.flash(str(error), 'error')
            self.view('post.edit.html', post=p)
            return

        self.flash('Well done my friend! Post: %s was Saved.'
                   % post.title, 'success')

        # Redirect to the new post page
        self.redirect(self.uri_for('post', id=post.key.id(), slug=post.slug))
        return
