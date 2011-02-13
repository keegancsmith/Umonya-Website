from django.conf.urls.defaults import *
from umonya.apply.views import *

urlpatterns = patterns('',
    ('^apply/students/', student_apply),
    ('^apply/teachers/', teacher_apply),
    ('^$', list_events),
)
