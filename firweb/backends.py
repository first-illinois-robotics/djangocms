import pickle
from typing import List

from django.core.cache.backends.memcached import BaseMemcachedCache
from django.core.mail import EmailMessage
from django.core.mail.backends.base import BaseEmailBackend


class GaeMemcachedCache(BaseMemcachedCache):
    """An implementation of a cache binding using google's app engine memcache lib (compatible with python-memcached)"""

    def __init__(self, server, params):
        from google.appengine.api import memcache
        super(GaeMemcachedCache, self).__init__(server, params,
                                                library=memcache,
                                                value_not_found_exception=ValueError)

    @property
    def _cache(self):
        if getattr(self, '_client', None) is None:
            self._client = self._lib.Client(self._servers, pickleProtocol=pickle.HIGHEST_PROTOCOL)
        return self._client


class GaeMailBackend(BaseEmailBackend):
    def send_messages(self, email_messages: List[EmailMessage]):
        """
        Send one or more EmailMessage objects and return the number of email
        messages sent.
        """
        for message in email_messages:
            from google import appengine
            mail = appengine.api.mail.EmailMessage()
            mail.to = message.to
            mail.subject = message.subject
            mail.body = message.body
            mail.sender = message.from_email
            mail.send()

