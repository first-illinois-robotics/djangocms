from firweb.wsgi import application
from google.appengine.api import wrap_wsgi_app

app = wrap_wsgi_app(application)
