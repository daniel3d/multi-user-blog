# appengine_config.py
from google.appengine.ext import vendor

""" Include 3th party libraries
	TO install: > pip install -t lib python-slugify
"""
vendor.add('lib')