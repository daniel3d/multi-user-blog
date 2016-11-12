# main.py

import os
import jinja2
import webapp2

from google.appengine.ext import db

viewer = jinja2.Environment(loader=jinja2.FileSystemLoader(
	os.path.join(os.path.dirname(__file__), 'views')), autoescape=True)

"""Base Controller functionality we need to reuse."""


class BaseController(webapp2.RequestHandler):

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


class HomeController(BaseController):

    def get(self):
        self.view('home.html', message="Hello, Daniel")

app = webapp2.WSGIApplication([('/', HomeController)], debug=True)
