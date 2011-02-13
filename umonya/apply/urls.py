from django.conf.urls.defaults import *
from umonya.apply.views import *

urlpatterns = patterns('',
    ('^student$', student_apply),
    ('^teacher$', teacher_apply),
)
