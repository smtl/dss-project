from django.utils.decorators import decorator_from_middleware

from signedcookies.middleware import SignedCookiesMiddleware

signed_cookies = decorator_from_middleware(SignedCookiesMiddleware)


