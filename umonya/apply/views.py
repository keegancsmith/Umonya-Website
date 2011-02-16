from umonya.apply.models import *
from umonya.apply.forms import *

from datetime import datetime
from django import forms
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, Context


def student_apply(request):
    if request.method == 'POST':
        form = StudentApplyForm(request.POST)
        if form.is_valid():
            pass # TODO save results of form
    else:
        form = StudentApplyForm()

    return render_to_response('apply.html', { 'form' : form })


def teacher_apply(request):
    
    if request.method == 'POST':
        form = TeacherApplyForm(request.POST)
        if form.is_valid():
            pass # TODO save results of form
    else:
        form = TeacherApplyForm()

    return render_to_response('apply.html', { 'form' : form })


def list_events(request):
    events = Event.objects.all()
    e = []
    i=0
    for x in events:
        e.append({})
        
        e[i]['date'] = x.start_datetime
        e[i]['location'] = x.location_id.address
        e[i]['description'] = ''
        e[i]['students_count'] = len(list(School.objects.filter(students__applications=x)))
        #e[i]['schools_count'] = Application.objects.filter(event_id=x).values('student_id').values('school_id').annotate(models.Count('school_id'))
        e[i]['schools_count'] = 0
        e[i]['close_date'] = x.end_datetime
        e[i]['id'] = str(x.location_id.address)+'-'+x.start_datetime.strftime('%Y-%m-%d')
        i+=1

    return render_to_response('events.html', { 'events' : e })
