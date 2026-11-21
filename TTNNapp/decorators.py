from functools import wraps
from flask import abort, session


def role_required(*allowed_roles):
    def decorator(view):
        @wraps(view)
        def wrapped_view(*args, **kwargs):
            if session.get("role") not in {role.upper() for role in allowed_roles}:
                abort(403)
            return view(*args, **kwargs)
        return wrapped_view
    return decorator
