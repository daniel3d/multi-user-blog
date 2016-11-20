# coding: utf-8

import os
import time
import random
import jinja2
import webapp2
from slugify import slugify
from webapp2_extras import sessions
from google.appengine.ext import db

"""
support init
~~~~~~~~
We include all nececery imports here so we can do initilization if needed.
"""

viewer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(
    os.path.dirname(__file__), '..', 'views')), autoescape=True)
"""Jinja2 template viwer that we can use in our controllers."""
