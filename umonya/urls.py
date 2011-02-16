from umonya.apply.views import *

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template


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

    # Direct to template
    (r'^$'            , direct_to_template, {'template':'home.html'}),
    (r'^contact-us'   , direct_to_template, {'template':'contact-us.html'}),
    (r'^get-involved' , direct_to_template, {'template':'get-involved.html'}),
    (r'^media'        , direct_to_template, {'template':'media.html'}),
    (r'^resources'    , direct_to_template, {'template':'resources.html'}),
    (r'^sponsors'     , direct_to_template, {'template':'sponsors.html'}),
    (r'^about-us'     , direct_to_template, {'template':'about-us.html'}),

    (r'^events/', include('umonya.apply.urls')),

    (r'^admin/', include(admin.site.urls)),
)
