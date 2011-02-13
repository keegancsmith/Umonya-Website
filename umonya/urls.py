from django.conf.urls.defaults import *
from umonya.apply.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Static files
    (r'^(?P<path>img/.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^(?P<path>css/.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^(?P<path>js/.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_DOC_ROOT}),
    (r'', include('umonya.apply.urls')),
    # Example:
    # (r'^umonya/', include('umonya.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
