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
    (r'^home', render_page, {'template':'home.html'}),
    (r'^contact-us', render_page, {'template':'contact-us.html'}),
    (r'^get-involved', render_page, {'template':'get-involved.html'}),
    (r'^$', render_page, {'template':'index.html'}),
    (r'^media', render_page, {'template':'media.html'}),
    (r'^resources', render_page, {'template':'resources.html'}),
    (r'^sponsors', render_page, {'template':'sponsors.html'}),
    (r'^about-us', render_page, {'template':'about-us.html'}),
    (r'^events/', include('umonya.apply.urls')),
    # Example:
    # (r'^umonya/', include('umonya.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
