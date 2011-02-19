from umonya.apply.models import *
from django.contrib import admin

for model in (Student, Event, Teacher, Reviewer, Review,
              Location, Region, School):
    admin.site.register(model)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'status', 'completed', 'email_sent',
                    'rsvped', 'active_ind')
    list_filter  = ('completed', 'email_sent', 'rsvped', 'active_ind')
admin.site.register(Application, ApplicationAdmin)
