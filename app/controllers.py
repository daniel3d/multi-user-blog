# controllers.py

import os
import jinja2
import webapp2

from models import Post
from slugify import slugify
from google.appengine.ext import db

viewer = jinja2.Environment(loader=jinja2.FileSystemLoader(
    os.path.join(os.path.dirname(__file__), 'views')), autoescape=True)

"""Base Controller functionality we need to reuse."""


class Controller(webapp2.RequestHandler):

    def write(self, *a, **kw):
        """Send response to the browser."""
        # self.request
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(*a, **kw)

    def view(self, template, **params):
        """Render template with given varibles."""
        view = viewer.get_template(template)
        self.write(view.render(params))

"""Home Controller."""


class HomeIndex(Controller):

    def get(self):
        self.view('post.html', title="Hello, Daniel")


"""Post Controller."""


class PostIndex(Controller):

    def get(self, post_id, slug=False):
        key = db.Key.from_path('Post', int(post_id))
        post = db.get(key)

        # We cannot find post in the database...
        if not post:
            self.error(404)
            return

        # If no slug redirect to the full slug url...
        if slug is False:
            self.redirect('/post/%s/%s' % (str(post_id), str(post.slug)))

        # Let display the post...
        self.view('post.html', post=post)


class PostNew(Controller):

    def get(self):
        self.view('post.edit.html', post=())

    def post(self):
        post = Post()
        post.title = self.request.get('title')
        post.slug = slugify(post.title)
        post.ribbon = self.request.get('ribbon')
        post.markdown = self.request.get('markdown')
        post.content = self.request.get('content') 
        post.put()

        self.redirect('/post/%s/%s' % (str(post.key().id()), post.slug))
        # error = "title, content or markdown not set!"
        # self.view('post.edit.html', error=error, title=title,
        #  markdown=markdown, content=content)


class PostEdit(PostNew):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id))
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.view('post.edit.html', post=post)

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id))
        post = db.get(key)

        if not post:
            self.error(404)
            return

        post.title = self.request.get('title')
        post.slug = slugify(post.title)
        post.ribbon = self.request.get('ribbon')
        post.markdown = self.request.get('markdown')
        post.content = self.request.get('content')
        post.put()

        self.redirect('/post/%s/%s' % (str(post.key().id()), post.slug))