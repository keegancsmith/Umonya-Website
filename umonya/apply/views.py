# Create your views here.
from django.http import HttpResponse
from django import forms
from django import template
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

def apply(request):
    if request.method == 'POST': # If the form has been submitted...
        form = StudentApplyForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            pass
    else:
        form = StudentApplyForm() # An unbound form
    t = template.loader.get_template('form.html')
    return HttpResponse(t.render(Context({'form': form})))
