from umonya.apply.models import *

from django import forms


class StudentApplyForm(forms.Form):
    first_name     = forms.CharField(max_length = 30)
    last_name      = forms.CharField(max_length = 30)
    school         = forms.CharField(max_length = 50)
    alt_event      = forms.BooleanField(
        label = 'Would you like to receive an email about alternate events '
                'if we can not accept you for this one?')
    grade          = forms.IntegerField()
    email          = forms.EmailField(label = 'Email address')
    concat_no      = forms.CharField(max_length = 20, label='Phone number')
    alt_contact_no = forms.CharField(
        max_length = 20,
        required   = False,
        label      = 'Parent\'s phone number')
    motivation     = forms.CharField(
        widget     = forms.widgets.Textarea(),
        max_length = 600,
        label      = 'Please explain briefly (max. 600 characters) why you '
                     'think you should be considered for this course.')


class TeacherApplyForm(forms.Form):
    first_name = forms.CharField(max_length = 30)
    last_name  = forms.CharField(max_length = 30)
    school     = forms.CharField(max_length = 50)
    email      = forms.EmailField(label = 'email address')
    concat_no  = forms.CharField(max_length = 20, label = 'Phone number')
