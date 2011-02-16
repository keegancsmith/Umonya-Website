from django.conf.urls.defaults import *
from umonya.apply.views import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Static files
    (r'^(?P<path>img/.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^(?P<path>css/.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^(?P<path>js/.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^$', render_page, {'template':'home.html'}),
    (r'^contact-us', render_page, {'template':'contact-us.html'}),
    (r'^get-involved', render_page, {'template':'get-involved.html'}),
    (r'^media', render_page, {'template':'media.html'}),
    (r'^resources', render_page, {'template':'resources.html'}),
    (r'^sponsors', render_page, {'template':'sponsors.html'}),
    (r'^about-us', render_page, {'template':'about-us.html'}),
    (r'^events/', include('umonya.apply.urls')),

    (r'^admin/', include(admin.site.urls)),
)
