from django.conf import settings
from django.conf.urls.defaults import include, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',

    (r'', include('umonya.content.urls')),
    (r'^events/', include('umonya.apply.urls')),

    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
