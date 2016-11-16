# coding: utf-8

import router
import webapp2

"""
gae-init
~~~~~~~~
Udacity Build Multi User Blog.
"""

__version__ = '0.0.1'


# Start the app
application = webapp2.WSGIApplication(router.ROUTES, debug=True)
