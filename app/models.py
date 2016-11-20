# models.py

import random
from google.appengine.ext import db

ribons = ["#f44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5", "#2196F3",
          "#00BCD4", "#009688", "#4CAF50", "#8BC34A", "#CDDC39", "#FFEB3B",
          "#FFC107", "#FF9800", "#FF5722", "#795548", "#9E9E9E", "#607D8B",
          "#2C3E50"]


class Post(db.Model):
    slug = db.StringProperty()
    ribbon = db.StringProperty()
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    markdown = db.TextProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def get_ribbon_style(self):
        if not self.ribbon:
            self.ribbon = random.choice(ribons)
            self.save()

        if self.ribbon[:1] == "#":
            return 'style="background-color: %s;"' % self.ribbon
        else:
            return 'style="background: url(%s) center / cover;"' % self.ribbon
