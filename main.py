from firweb.wsgi import application
from google.appengine.api import wrap_wsgi_app  # type: ignore

app = wrap_wsgi_app(application)
