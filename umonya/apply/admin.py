from umonya.apply.models import *
from django.contrib import admin

for model in (Student, Event, Teacher, Reviewer, Application, Review,
              Location, Region, School):
    admin.site.register(model)
