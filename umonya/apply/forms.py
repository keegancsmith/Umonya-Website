from umonya.apply.models import *

from django import forms
from uni_form.helpers import FormHelper, Submit


class UniFormSubmitForm(forms.Form):

    @property
    def helper(self):
        helper = FormHelper()
        submit = Submit('submit', 'Submit your application')
        helper.add_input(submit)
        helper.form_action = self.form_action
        helper.form_method = 'POST'
        return helper


class StudentApplyForm(UniFormSubmitForm):
    first_name     = forms.CharField(max_length=30)
    last_name      = forms.CharField(max_length=30)
    school         = forms.CharField(max_length=50)
    alt_event      = forms.BooleanField(
        label='Would you like to receive an email about alternate events '
              'if we can not accept you for this one?',
        required=False)
    grade          = forms.IntegerField()
    email          = forms.EmailField(label='Email address')
    contact_no     = forms.CharField(max_length=20, label='Phone number')
    alt_contact_no = forms.CharField(
        max_length = 20,
        required   = False,
        label      = 'Parent\'s phone number')
    motivation     = forms.CharField(
        widget     = forms.widgets.Textarea(),
        max_length = 600,
        label      = 'Please explain briefly (max. 600 characters) why you '
                     'think you should be considered for this course.')

    form_action = 'apply'


class TeacherApplyForm(UniFormSubmitForm):
    first_name = forms.CharField(max_length=30)
    last_name  = forms.CharField(max_length=30)
    school     = forms.CharField(max_length=50)
    email      = forms.EmailField(label='email address')
    contact_no = forms.CharField(max_length=20, label='Phone number')

    form_action = 'apply'
