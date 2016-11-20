# router.py

import controllers as ctr

ROUTES = [
    ('/', ctr.HomeIndex),
    ('/post/new', ctr.PostNew),
    ('/post/([0-9]+)', ctr.PostIndex),
    ('/post/([0-9]+)/edit', ctr.PostEdit),
    ('/post/([0-9]+)/delete', ctr.PostDelete),
    ('/post/([0-9]+)/(?P<slug>[+\-\w]+)', ctr.PostIndex)
]
