from django.conf.urls.defaults import *
from umonya.apply.views import *

urlpatterns = patterns('',
    ('^([^/]+)/student-apply/', student_apply),
    ('^([^/]+)/teacher-apply/', teacher_apply),
    ('^$', list_events),
)
