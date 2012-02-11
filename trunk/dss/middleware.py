import re
try:
    from hashlib import md5 as hash
except ImportError:
    from md5 import new as hash

from django.conf import settings

regex = re.compile(r'([0-9a-f]+):(.*)$')

class SignedCookiesMiddleware(object):

    def process_request(self, request):
        for (key, signed_value) in request.COOKIES.items():
            try:
                (signature, value) = regex.match(signed_value).groups()
                assert signature == self.get_digest(key, value)
                request.COOKIES[key] = value
            except:
                del request.COOKIES[key]

    def process_response(self, request, response):
        for (key, morsel) in response.cookies.items():
            if morsel['expires'] == 0 and morsel['max-age'] == 0:
                continue
            digest = self.get_digest(key, morsel.value)
            response.set_cookie(key, '%s:%s' % (digest, morsel.value),
                max_age=morsel['max-age'],
                expires=morsel['expires'],
                path=morsel['path'],
                domain=morsel['domain'],
                secure=morsel['secure']
            )
        return response

    def get_digest(self, key, value):
        string = ':'.join([settings.SECRET_KEY, key, value])
        return hash(string).hexdigest() 
