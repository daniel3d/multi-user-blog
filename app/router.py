# coding: utf-8
"""The app routes."""

import controllers as ctr
from support import webapp2

ROUTES = [
    # Blog routers
    webapp2.Route('/', ctr.HomeIndex, name='blog'),
    webapp2.Route('/post/new', ctr.PostNew, name='post.new'),
    webapp2.Route('/post/<id:[0-9]+>', ctr.PostIndex, name='post.find'),
    webapp2.Route('/post/<id:[0-9]+>/edit', ctr.PostEdit, name='post.edit'),
    webapp2.Route('/post/<id:[0-9]+>/delete',
                  ctr.PostDelete, name='post.delete'),
    webapp2.Route('/post/<id:[0-9]+>/<slug:[+\-\w]+>',
                  ctr.PostIndex, name='post'),
    # Auth routers
    webapp2.Route('/login', ctr.UserLoginIndex, name='auth.login'),
    webapp2.Route('/logout', ctr.UserLogoutIndex, name='auth.logout'),
    webapp2.Route('/register', ctr.UserRegisterIndex, name='auth.register'),
    #webapp2.Route('/password', ctr.UserSetPassword),
    #webapp2.Route('/forgot', ctr.UserForgotPassword, name='auth.forgot'),
    webapp2.Route('/<operation:v|p>/<user_id:\d+>-<token:.+>',
                  handler=ctr.UserVerification, name='auth.verification')
]
