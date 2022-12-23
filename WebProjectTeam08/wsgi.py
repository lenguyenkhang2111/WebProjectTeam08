"""
WSGI config for WebProjectTeam08 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from dj_static import Cling, MediaCling
from static_ranges import Ranges
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebProjectTeam08.settings')
application = Ranges(Cling(MediaCling(get_wsgi_application())))
