from umonya.apply.models import *
from umonya.apply.forms import *

from datetime import datetime
from django import forms
from django.db import models, transaction
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context


def add_update_student(data, event):
    '''
    Adds or updates an application, using the cleaned_data from a valid
    StudentApplyForm
    '''
    # method for random fields i don't understand the reason for existance
    import random
    def random_str(length):
        import string
        return ''.join(random.choice(string.ascii_lowercase)
                       for i in range(length))

    # XXX Some defaults until some discussion takes place on the db design, or
    # what to ask in the application form
    region = Region.objects.get_or_create(name = 'Western Cape')[0]
    referral_source = ReferralSource.objects.get_or_create(
        description = 'Trolling')[0]
    status = Status.objects.get_or_create(description = 'Noob')[0]

    school = School.objects.get_or_create(name = data['school'],
                                          region = region)[0]

    # XXX if a student already exists, should this create an error? At the
    # moment this just creates a new student with a different student id
    student = Student.objects.create(
        student_id     = random_str(30),
        first_name     = data['first_name'],
        last_name      = data['last_name'],
        school         = school,
        alt_event      = data['alt_event'],
        grade          = data['grade'],
        email          = data['email'],
        contact_no     = data['contact_no'],
        alt_contact_no = data['alt_contact_no'])


    application = Application.objects.create(
        student         = student,
        event           = event,
        motivation      = data['motivation'],
        referral_source = referral_source,
        teacher         = None,
        status          = status,
        status_reviewer = None)


@transaction.commit_on_success
def student_apply(request, event_slug):
    try:
        event = Event.get_by_slug(event_slug)
    except Event.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = StudentApplyForm(request.POST)
        if form.is_valid():
            add_update_student(form.cleaned_data, event)

            # XXX where should the student go to after applying?
            return HttpResponseRedirect('/')
    else:
        form = StudentApplyForm()

    return render_to_response('apply.html', { 'form' : form })


def teacher_apply(request, event):
    try:
        event = Event.get_by_slug(event_slug)
    except Event.DoesNotExist:
        raise Http404
    
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

    for x in events:
        e.append({
                'date'          : x.start_datetime,
                'location'      : x.location.address,
                'description'   : '',
                'student_count' : x.applications.count(),
                'school_count'  : x.school_count,
                'close_date'    : x.end_datetime,
                'id'            : x.slug,
        })

    return render_to_response('events.html', { 'events' : e })
