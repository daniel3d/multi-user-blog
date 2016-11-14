# appengine_config.py
from google.appengine.ext import vendor

""" Include 3th party libraries
	make sure you run first
	pip install -t lib -r requirements.txt
"""
vendor.add('lib')