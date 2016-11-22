# models.py

from support import db, random, config

"""Posts db model."""


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
            self.ribbon = random.choice(config.COLOR_PALETTE)
            self.save()

        if self.ribbon[:1] is "#":
            return 'style="background-color: %s;"' % self.ribbon
        else:
            return 'style="background: url(%s) center / cover;"' % self.ribbon

"""Users db model."""


class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email=None):
        pw_hash = make_pw_hash(name, pw)
        user = User(parent=users_key(), name=name, pw_hash=pw_hash, email=email)
        user.put()
        return user

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u
