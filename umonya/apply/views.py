from django.http import HttpResponse
from django import forms
from django.template import loader, Context
from umonya.apply.models import Student, Application, Event
from django.db import models

class StudentApplyForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    school = forms.CharField(max_length=50)
    alt_event = forms.BooleanField(label='Would you like to receive an email about alternate events if we can not accept you for this one?')
    grade = forms.IntegerField()
    email = forms.EmailField(label='Email address')
    concat_no = forms.CharField(max_length=20, label='Phone number')
    alt_contact_no = forms.CharField(max_length=20, required=False, label='Parent\'s phone number')

def student_apply(request):
    if request.method == 'POST':
        form = StudentApplyForm(request.POST)
        if form.is_valid():
            pass # TODO save results of form
    else:
        form = StudentApplyForm()
    t = loader.get_template('apply.html')
    return HttpResponse(t.render(Context({'form': form})))

class TeacherApplyForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    school = forms.CharField(max_length=50)
    email = forms.EmailField(label='email address')
    concat_no = forms.CharField(max_length=20, label='Phone number')

def teacher_apply(request):
    if request.method == 'POST':
        form = TeacherApplyForm(request.POST)
        if form.is_valid():
            pass # TODO save results of form
    else:
        form = TeacherApplyForm()
    t = loader.get_template('apply.html')
    return HttpResponse(t.render(Context({'form': form})))

def list_events(request):
    events = Event.objects.all()
    e = []
    i=0
    for x in events:
        e.append({})
        
        e[i]['date'] = x.start_datetime
        e[i]['location'] = x.location_id.address
        e[i]['description'] = ''
        e[i]['students_count'] = len(list(Application.objects.filter(event_id=x)))
        #e[i]['schools_count'] = Application.objects.filter(event_id=x).values('student_id').values('school_id').annotate(models.Count('school_id'))
        e[i]['schools_count'] = 0
        e[i]['close_date'] = x.end_datetime
        i+=1
    t = loader.get_template('events.html')
    return HttpResponse(t.render(Context({'events':e})))
