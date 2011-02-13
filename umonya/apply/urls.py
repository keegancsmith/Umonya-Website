from django.conf.urls.defaults import *
from umonya.apply.views import *

urlpatterns = patterns('',
    ('^events/apply/students/', student_apply),
    ('^events/apply/teachers/', teacher_apply),
    ('^events/$', list_events),
)
