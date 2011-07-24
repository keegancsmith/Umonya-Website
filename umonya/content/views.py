from annoying.decorators import render_to

from umonya.content.models import Sponsor


@render_to('sponsors.html')
def sponsors(request):
    return {
        'sponsors': Sponsor.objects.filter(type='Sponsor'),
        'collaborators': Sponsor.objects.filter(type='Collaborator'),
    }
