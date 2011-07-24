from django.conf.urls.defaults import include, patterns
from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
    'umonya.content.views',

    (r'^sponsors'     , 'sponsors'),

    # Direct to template
    (r'^$'            , direct_to_template, {'template':'home.html'}),
    (r'^contact-us'   , direct_to_template, {'template':'contact-us.html'}),
    (r'^get-involved' , direct_to_template, {'template':'get-involved.html'}),
    (r'^media'        , direct_to_template, {'template':'media.html'}),
    (r'^resources'    , direct_to_template, {'template':'resources.html'}),
    (r'^about-us'     , direct_to_template, {'template':'about-us.html'}),
)
