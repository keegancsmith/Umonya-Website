import datetime

from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    region  = models.ForeignKey(Region, related_name="locations")
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return self.address


class Status(models.Model):
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.description


class ReferralSource(models.Model):
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.description


class School(models.Model):
    name   = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name="schools")

    def __unicode__(self):
        return self.name


class Student(models.Model):
    student_id     = models.CharField(max_length=36, unique=True)
    first_name     = models.CharField(max_length=30, null=True, blank=True)
    last_name      = models.CharField(max_length=30, null=True, blank=True)
    school         = models.ForeignKey(School, related_name="students", null=True, blank=True)
    alt_event      = models.BooleanField(default=False)
    grade          = models.IntegerField(null=True, blank=True)
    email          = models.EmailField()
    contact_no     = models.CharField(max_length=20, null=True, blank=True)
    alt_contact_no = models.CharField(max_length=20, null=True, blank=True)
    active_ind     = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s %s (%s)' % (self.first_name, self.last_name, self.school.name)


class Event(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime   = models.DateTimeField()
    location       = models.ForeignKey(Location, related_name="events")
    url            = models.URLField(max_length=100)
    active_ind     = models.BooleanField(default=True)

    @classmethod
    def get_by_slug(cls, slug):
        location, year, month, day = slug.rsplit('-', 4)
        try:
            return cls.objects.filter(location__address__exact=location,
                                      start_datetime__year=year,
                                      start_datetime__month=month,
                                      start_datetime__day=day).get()
        except ValueError:
            raise Event.DoesNotExist

    @property
    def school_count(self):
        return (School.objects
                .filter(students__applications__event=self)
                .count())

    @property
    def slug(self):
        return u'%s-%s' % (self.location.address,
                           self.start_datetime.strftime('%Y-%m-%d'))

    def __unicode__(self):
        return self.slug


class Teacher(models.Model):
    teacher    = models.CharField(max_length=36, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name  = models.CharField(max_length=30, null=True, blank=True)
    school     = models.ForeignKey(School, related_name="teachers", null=True, blank=True)
    email      = models.EmailField()
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    active_ind = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s %s (%s)' % (self.first_name, self.last_name,
                               self.school.name)


# TODO: login
class Reviewer(models.Model):
    name           = models.CharField(max_length=30)
    email          = models.EmailField()
    admin          = models.BooleanField(default=False)
    event_admin    = models.ManyToManyField(Event, related_name="admins")
    event_reviewer = models.ManyToManyField(Event, related_name="reviewers")

    def __unicode__(self):
        return self.name


class Application(models.Model):
    student            = models.ForeignKey(Student, related_name="applications")
    event              = models.ForeignKey(Event, related_name="applications")
    creation_datetime  = models.DateTimeField(default = datetime.datetime.now)
    motivation         = models.TextField(null=True, blank=True)
    special_motivation = models.TextField(null=True, blank=True)
    referral_source    = models.ForeignKey(ReferralSource, related_name="applications")
    teacher            = models.ForeignKey(Teacher, related_name="student_applications", null=True)
    status             = models.ForeignKey(Status)
    status_reviewer    = models.ForeignKey(Reviewer, related_name="applications_reviewed", null=True)
    completed          = models.BooleanField(default=False)
    email_sent         = models.BooleanField(default=False)
    rsvped             = models.BooleanField(default=False)
    active_ind         = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s for %s' % (unicode(self.student), unicode(self.event))


class Review(models.Model):
    application       = models.ForeignKey(Application, related_name="reviews")
    event             = models.ForeignKey(Event, related_name="reviews")
    creation_datetime = models.DateTimeField()
    reviewer          = models.ForeignKey(Reviewer, related_name="reviews")
    status            = models.ForeignKey(Status, null=True, blank=True)
    comment           = models.TextField(null=True, blank=True)
    rating            = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s - %s' % (unicode(self.status), unicode(self.application))
