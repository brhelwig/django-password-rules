import django
from django.conf import settings

settings.configure()

try:
    django.setup()
except AttributeError:  # django 1.4
    pass
