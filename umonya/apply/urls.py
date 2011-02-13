from django.conf.urls.defaults import *
from umonya.apply.views import *

urlpatterns = patterns('',
    ('^apply/student$', student_apply),
    ('^apply/teacher$', teacher_apply),
    ('^events/$', list_events),
)
