"""
datetimex.api
~~~~~~~~~~~~~

Improved datetimes

"""
import pytz
import datetime as dt
import time

from datetime import datetime
from forbiddenfruit import curse


def get_timezone(timezone):
    if isinstance(timezone, dt.tzinfo) or timezone is None:
        return timezone
    else:
        return pytz.timezone(timezone)

@classmethod
def now(cls, timezone=None):
    return datetime.fromtimestamp(time.time(), get_timezone(timezone))


def to(self, timezone):
    return self.replace(tzinfo=get_timezone(timezone))


def patch():
    curse(datetime, 'now', now)
    curse(datetime, 'to', to)