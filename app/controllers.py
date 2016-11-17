# controllers.py

# for debuging only
import logging
from pprint import pprint

# General imports
import webapp2
from models import Post
from slugify import slugify
from google.appengine.ext import db
from support import viewer, helpers, config

"""Base Controller functionality we need to reuse."""


class Controller(webapp2.RequestHandler):

    def write(self, *a, **kw):
        """Send response to the browser."""
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(*a, **kw)

    def view(self, template, **params):
        """Render template with given varibles."""
        view = viewer.get_template(template)
        self.write(view.render(params))

    def set_secure_cookie(self, name, val):
        """Set secure cookie."""
        cookie_val = helpers.make_secure_value(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        """Read secure cookie."""
        cookie_val = self.request.cookies.get(name)
        return cookie_val and helpers.check_secure_value(cookie_val)

    def login(self, user):
        """Login the user by setting up a secure cookie."""
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        """Logout the user by removing the secure cookie."""
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

"""Home Controller."""


class HomeIndex(Controller):

    def get(self):
        logging.info(helpers.make_secure_value('test'))
        self.view('post.html', post=())




















"""Post Controller."""


class PostIndex(Controller):

    def get(self, post_id, slug=False):
        key = db.Key.from_path('Post', int(post_id))
        post = db.get(key)
        #logging.info("------------------------")
        #logging.info(post.to_xml())
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
        """Save new Post to the database. """

        post = {
            "title": self.request.get('title').strip(),
            "slug": slugify(self.request.get('title')),
            "ribbon": self.request.get('ribbon').strip(),
            "markdown": self.request.get('markdown').strip(),
            "content": self.request.get('content').strip()
        }

        try: # Try saving the post
            s_post = Post(markdown=post["markdown"], content=post["content"], 
                ribbon=post["ribbon"], title=post["title"], slug=post["slug"])
            s_post.put()
        except Exception, error:
            self.view('post.edit.html', errors=[str(error)], post=post)
            return

        # Redirect to the new post page
        self.redirect('/post/%s/%s' % (str(s_post.key().id()), s_post.slug))

class PostEdit(PostNew):

    def get(self, post_id):
        post = Post()
        #post.get_by_id(int(post_id))
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
