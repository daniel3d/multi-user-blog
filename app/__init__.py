# -*- coding: utf-8 -*-
"""Initilize the blog application."""

import router
from support import webapp2, config

"""
gae-init
~~~~~~~~
Udacity Build Multi User Blog.
"""

__version__ = config.VERSION

# Start the app
application = webapp2.WSGIApplication(router.ROUTES, config={
    'webapp2_extras.auth': {
        'user_model': 'app.models.User',
        'user_attributes': ['name']
    },
    'webapp2_extras.sessions': {
        'secret_key': config.APP_KEY
    }
}, debug=True)
