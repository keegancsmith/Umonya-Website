from django.db import models


SPONSOR_TYPE_CHOICES = (
    ('Sponsor', 'Sponsor'),
    ('Collaborator', 'Collaborator'),
)
class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image_path = models.CharField(max_length=100)
    years = models.CharField(max_length=50)
    type = models.CharField(max_length=15, choices=SPONSOR_TYPE_CHOICES)

    def __unicode__(self):
        return '%s %s' % (self.type, self.name)
