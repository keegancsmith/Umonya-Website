from umonya.apply.models import *
from django.contrib import admin

for model in Student, Event, Teacher, Reviewer, Application, Review:
    admin.site.register(model)
