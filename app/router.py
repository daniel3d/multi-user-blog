# router.py

import controllers as ctr

ROUTES = [
    # Home page ulog.com/
    ('/', ctr.HomeIndex),
    # Capture ulog.com/post/`id`/`slug`
    ('/post/new', ctr.PostNew),
    ('/post/([0-9]+)', ctr.PostIndex),
    ('/post/([0-9]+)/edit', ctr.PostEdit),
    ('/post/([0-9]+)/(?P<slug>[+\-\w]+)', ctr.PostIndex)
]
