import time
from django.conf import settings
from django.contrib import messages

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_expiry_age = getattr(settings, 'SESSION_COOKIE_AGE', 1800)  # Default 30 minutes
        session_warn_at = session_expiry_age - 60  # Warn 1 minute before expiry

        last_activity = request.session.get('last_activity')
        if last_activity:
            now = time.time()
            elapsed = now - last_activity
            if elapsed > session_warn_at:
                messages.warning(request, 'Your session will expire soon. Please save your work.')

        # Update last activity timestamp
        request.session['last_activity'] = time.time()

        response = self.get_response(request)
        return response
