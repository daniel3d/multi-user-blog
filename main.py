# main.py

import os
import jinja2
import webapp2

templates = os.path.join(os.path.dirname(__file__), 'views')
viewer = jinja2.Environment(loader=jinja2.FileSystemLoader(templates))

"""Common Handler functionality to extend our controllers."""


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        # self.request
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(*a, **kw)

    def view(self, template, **params):
        view = viewer.get_template(template)
        self.write(view.render(params))

"""Home Page Controller."""


class HomePage(Handler):

    def get(self):
        self.view('home.html', message="Hello, Daniel")

app = webapp2.WSGIApplication([('/', HomePage)], debug=True)
