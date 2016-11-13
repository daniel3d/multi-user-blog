# router.py

import controllers as ctr

ROUTES = [
    # Home page ulog.com/
    ('/', ctr.HomePageIndex),
    # Capture ulog.com/post/`id`/`slug`
    ('/post/new', ctr.PostPageNew),
    ('/post/([0-9]+)', ctr.PostPageIndex),
    ('/post/([0-9]+)/(?P<slug>[+\-\w]+)', ctr.PostPageIndex)
]
