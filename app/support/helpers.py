# helpers.py

import hmac
from config import APP_KEY

def make_secure_value(val):
    return '%s:%s' % (val, hmac.new(APP_KEY, val).hexdigest())

def check_secure_value(sec):
    val = sec.split(':')[0]
    if sec == make_secure_value(val):
        return val