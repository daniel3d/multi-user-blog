# coding: utf-8

import router
import webapp2
from support import config

"""
gae-init
~~~~~~~~
Udacity Build Multi User Blog.
"""

__version__ = '0.0.1'

# Start the app
application = webapp2.WSGIApplication(router.ROUTES, config={
	'webapp2_extras.sessions': {
		'secret_key': config.APP_KEY
	}
}, debug=True)
