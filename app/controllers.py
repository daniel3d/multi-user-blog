# controllers.py

from models import db, Post, User
from support import viewer, helpers, config, slugify, sessions, webapp2, time

"""Base Controller functionality we need to reuse."""


class Controller(webapp2.RequestHandler):

    def write(self, *a, **kw):
        """Send response to the browser."""
        self.response.out.write(*a, **kw)

    def view(self, template, **params):
        """Render template with given varibles."""
        view = viewer.get_template(template)
        self.write(view.render(params, messages=self.flash_messages))

    def dispatch(self):
        """Get a session store for this request."""
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        """Returns a session using the default cookie key."""
        return self.session_store.get_session()

    @webapp2.cached_property
    def flash_messages(self):
        """Implement flash messages."""
        return self.session.get_flashes(key='_messages')

    def flash(self, message, level='warning'):
        """Flash message."""
        self.session.add_flash(message, level, key='_messages')

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

"""Home Controller."""


class HomeIndex(Controller):

    def get(self):
        """Display most reacent posts."""
        posts = Post.all().order('-created_at')
        self.view('home.html', posts=posts)
        return

"""Base controller for posts."""


class PostIndex(Controller):

    def get(self, id, slug=False):
        """Display existing post."""
        post = self.get_post_by_id(id)
        # We cannot find post in the database...
        if not post:
            self.error(404)
            return
        # If no slug redirect to the full slug url...
        if slug is False:
            self.redirect('/post/%s/%s' % (str(id), str(post.slug)))
        # Let display the post...
        self.view('post.html', post=post)

    def get_post_by_id(self, post_id):
        """Commonly used function to retrive post by id."""
        return db.get(db.Key.from_path('Post', int(post_id)))

"""Create new post."""


class PostNew(PostIndex):

    def get(self):
        """Get the new post form."""
        self.view('post.edit.html', post=())
        return

    def post(self):
        """Save new Post to the database. """
        p = {
            "title": self.request.get('title').strip(),
            "slug": slugify(self.request.get('title')),
            "ribbon": self.request.get('ribbon'),
            "markdown": self.request.get('markdown').strip(),
            "content": self.request.get('content').strip()
        }
        try:  # Try saving the post
            post = Post(ribbon=p["ribbon"], markdown=p["markdown"],
                        title=p["title"], content=p["content"], slug=p["slug"])
            post.put()
        except Exception, error:
            self.flash(str(error), 'error')
            self.view('post.edit.html', post=p)
            return
        self.flash('Well done my friend! Post: %s was Saved.' % post.title,
                   'success')
        # Redirect to the new post page
        self.redirect('/post/%s/%s' % (str(post.key().id()), post.slug))
        return

"""Update existing post."""


class PostEdit(PostNew):

    def get(self, id):
        """Open edit form for the the post."""
        post = self.get_post_by_id(id)
        if not post:
            self.error(404)
            return
        self.view('post.edit.html', post=post)
        return

    def post(self, id):
        """Submit the eddited post."""
        post = self.get_post_by_id(id)
        if not post:
            self.error(404)
            return
        post.title = self.request.get('title').strip()
        post.slug = slugify(post.title).strip()
        post.ribbon = self.request.get('ribbon').strip()
        post.markdown = self.request.get('markdown').strip()
        post.content = self.request.get('content').strip()
        post.put()
        self.flash('Well done my friend! Post: %s was Updated.' % post.title,
                   'success')
        self.redirect('/post/%s/%s' % (str(post.key().id()), post.slug))
        return

"""Delete existing post."""


class PostDelete(PostIndex):

    def get(self, id):
        post = self.get_post_by_id(id)
        post.delete()
        self.flash('Post: %s was Deleted.' % post.title, 'warning')
        time.sleep(0.5)
        self.redirect('/')
        return

"""Base controller for Auth functionality."""


class AuthIndex(Controller):

    def login(self, user):
        """Login the user by setting up a secure cookie."""
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        """Logout the user by removing the secure cookie."""
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def valid_username(self, username):
        """Check if the username is valid."""
        return username and config.REGEXR_USERNAME.match(username)

    def valid_password(self, password):
        """Check if the password is valid."""
        return password and config.REGEXR_PASSWORD.match(password)

    def valid_email(self, email):
        """Check if the email is valid."""
        return not email or config.REGEXR_EMAIL.match(email)

"""Login page."""


class LoginIndex(AuthIndex):

    def get(self):
        self.view('login.html')
        return

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        user = User.login(username, password)
        if user:
            self.login(user)
            self.redirect('/')
        else:
            message = 'Invalid Username or Password'
            self.view('login.html', error=message, username=username)

"""Register page."""


class RegisterIndex(AuthIndex):

    def get(self):
        self.view('register.html')

    def post(self):
        valid = True
        username = self.request.get('username').strip()
        email = self.request.get('email').strip()
        password = self.request.get('password').strip()
        re_password = self.request.get('password-validate').strip()

        params = dict(username=username, email=email)

        if User.by_name(username):
            self.view('register.html', error_username='Username already taken.')
        
        if not self.valid_username(username):
            params['error_username'] = "That's not a valid username."
            valid = None
        
        if not self.valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            valid = None
        elif password != re_password:
            params['error_password_verify'] = "Your passwords didn't match."
            valid = None

        if not self.valid_email(email):
            params['error_email'] = "That's not a valid email."
            valid = None
        
        if not valid:
            self.view('register.html', **params)
        else:
            self.login(User.register(username, password, email))
            self.redirect('/')

"""Logout page."""


class LogoutIndex(AuthIndex):

    def post(self):
        self.logout()
        self.redirect('/login')
        return
