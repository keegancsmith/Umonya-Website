# Create your views here.
from django import newforms as forms
from umonya.apply.models import Student, Application

def apply(request):
    ApplyForm = forms.form_for_model(Application)

    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApplyForm()

    return render_to_response('form.html', { 'form' : form })
