from django.conf.urls import *
from django.conf import settings
from django.views.generic.base import RedirectView
from django.http import HttpResponse
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

handler500 = 'app.views.handler_500'
handler404 = 'app.views.handler_404'

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('app.urls')),
    #url(r'^enewsletter/', include('newsletter.urls')),
    url(r'^lwinmoe/doc/lwinmoe-thesis.pdf$', RedirectView.as_view(url='http://lwinmoe.org/static/docs/lwinmoe-thesis.pdf', permanent=True)),
    url(r'^sheriff/', include(admin.site.urls)),
    #url(r'^assets/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes':False}),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
]



