import os
import jinja2

viewer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(
	os.path.dirname(__file__), '..', 'views')), autoescape=True)