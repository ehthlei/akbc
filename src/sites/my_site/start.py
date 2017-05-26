import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_site.settings'

def add_python_path():
  import sys, os
  import site
  root = os.path.dirname(os.path.dirname(__file__))
  paths = (os.path.join(root, "packages"),)
  for path in paths:
    if not path in sys.path:
        sys.path.insert(0, path)
  site.addsitedir(os.path.join(root, "packages"))

  packages = os.path.join(root, "packages")
  # 3rd party libraries
  sys.path.insert(0, os.path.join(packages, "httplib2.zip"))
  sys.path.insert(0, os.path.join(packages, "oauth2.zip"))
  sys.path.insert(0, os.path.join(packages, "openid.zip"))
  sys.path.insert(0, os.path.join(packages, "markdown.zip"))
  sys.path.insert(0, os.path.join(packages, "djangoratings.zip"))
  sys.path.insert(0, os.path.join(packages, "taggit.zip"))
  sys.path.insert(0, os.path.join(packages, "pytz.zip"))
  sys.path.insert(0, os.path.join(packages, "simplejson.zip"))
  sys.path.insert(0, os.path.join(packages, "requests.zip"))
  sys.path.insert(0, os.path.join(packages, "fudge.zip"))


# modify path
add_python_path()

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()