# controllers.py

import os
import jinja2
import webapp2

from models import Post

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


class HomePageIndex(Controller):

    def get(self):
        self.view('post.html', title="Hello, Daniel")


"""Post Controller."""


class PostPageIndex(Controller):

    def get(self, post_id, slug=False):

        # If no slug redirect to the full slug url...
        if slug is False:
            self.redirect('/post/%s/%s' % (int(post_id), "some-cool-slug"))

        # Let display the post...
        self.view('post.html', title=slug,
                  ribbon="background:url(https://s.yimg.com/uy/build/images/sohp/hero/lax-den3.jpg) no-repeat center center fixed;")


class PostPageNew(Controller):

    def get(self):
        self.view('post.new.html', title="New Post: Write someting awsome",
                  ribbon="background-color: #795548;")
