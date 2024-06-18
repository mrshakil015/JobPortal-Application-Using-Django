import time
from django.conf import settings

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_expiry_age = getattr(settings, 'SESSION_COOKIE_AGE', 1800)  # Default 30 minutes

        last_activity = request.session.get('last_activity')
        if last_activity:
            now = time.time()
            elapsed = now - last_activity
            if elapsed > session_expiry_age:
                request.session.flush()  # Clear the session data
                request.session['last_activity'] = now  # Update last activity timestamp
                return self.get_response(request)

        request.session['last_activity'] = time.time()  # Update last activity timestamp

        response = self.get_response(request)
        return response
