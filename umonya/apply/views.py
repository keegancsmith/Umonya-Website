# Create your views here.
from django.http import HttpResponse
from django import forms
from django.template import loader, Context
from umonya.apply.models import Student, Application

class StudentApplyForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    school = forms.CharField(max_length=50)
    alt_event = forms.BooleanField()
    grade = forms.IntegerField()
    email = forms.EmailField()
    concat_no = forms.CharField(max_length=20)
    alt_contact_no = forms.CharField(max_length=20, required=False)

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
    email = forms.EmailField()
    concat_no = forms.CharField(max_length=20)

def teacher_apply(request):
    if request.method == 'POST':
        form = TeacherApplyForm(request.POST)
        if form.is_valid():
            pass # TODO save results of form
    else:
        form = TeacherApplyForm()
    t = loader.get_template('apply.html')
    return HttpResponse(t.render(Context({'form': form})))
