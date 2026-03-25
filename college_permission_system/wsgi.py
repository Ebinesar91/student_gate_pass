"""
WSGI config for college_permission_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_permission_system.settings')

# 🚀 Self-Migrating wsgi file for Vercel!
if "VERCEL" in os.environ:
    from django.core.management import call_command
    import django
    django.setup()
    try:
        call_command('migrate', interactive=False)
    except Exception as e:
        print(f"Migration Error: {e}")

application = get_wsgi_application()
