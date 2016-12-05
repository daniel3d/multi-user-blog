# -*- coding: utf-8 -*-
"""Initilize the blog application."""

import router
import config
import webapp2

"""
gae-init
~~~~~~~~
Udacity Build Multi User Blog.
"""

__version__ = config.VERSION
"""Set for google app engine the version of the application."""

application = webapp2.WSGIApplication(router.ROUTES, config={
    'webapp2_extras.auth': {
        'user_model': 'app.models.User',
        'user_attributes': ['name']
    },
    'webapp2_extras.sessions': {
        'secret_key': config.APP_KEY
    }
}, debug=config.DEV)
"""Start the application."""
