# coding: utf-8
"""The app routes."""

import webapp2

from handlers import HomeHandler, PostHandler, NewPostHandler, LikePostHandler, 
  EditPostHandler, DeletePostHandler, CommentPostHandler, LoginUserHandler, 
  LogoutUserHandler, RegisterUserHandler, VerificateUserHandler

ROUTES = [
    # Blog routers
    webapp2.Route('/', HomeHandler, name='blog'),
    webapp2.Route('/post/new', NewPostHandler, name='post.new'),
    webapp2.Route('/post/<id:[0-9]+>', PostHandler, name='post.find'),
    webapp2.Route('/post/<id:[0-9]+>/edit', EditPostHandler, name='post.edit'),
    webapp2.Route('/post/<id:[0-9]+>/delete',
                  DeletePostHandler, name='post.delete'),
    webapp2.Route('/post/<id:[0-9]+>/like',
                  LikePostHandler, name='post.like'),
    webapp2.Route('/post/<id:[0-9]+>/comment',
                  CommentPostHandler, name='post.comment'),
    webapp2.Route('/post/<id:[0-9]+>/<slug:[+\-\w]+>',
                  PostHandler, name='post'),
    # Auth routers
    webapp2.Route('/login', LoginUserHandler, name='auth.login'),
    webapp2.Route('/logout', ctr.UserLogoutIndex, name='auth.logout'),
    webapp2.Route('/register', RegisterUserHandler, name='auth.register'),
    webapp2.Route('/<operation:v|p>/<user_id:\d+>-<token:.+>',
                  handler=ctr.UserVerification, name='auth.verification')
]
