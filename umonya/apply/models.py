from django.db import models

class Student(models.Model):
    student_id     = models.CharField(max_length=36, unique=True)
    first_name     = models.CharField(max_length=30, null=True, blank=True)
    last_name      = models.CharField(max_length=30, null=True, blank=True)
    school_id      = models.ForeignKey(School, related_name="students", null=True, blank=True)
    alt_event      = models.BooleanField(default=False)
    grade          = models.IntegerField(null=True, blank=True)
    email          = models.EmailField()
    contact_no     = models.CharField(max_length=20, null=True, blank=True)
    alt_contact_no = models.CharField(max_length=20, null=True, blank=True)
    active_ind     = models.BooleanField(default=True)

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=36, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name  = models.CharField(max_length=30, null=True, blank=True)
    school_id  = models.ForeignKey(School, related_name="teachers", null=True, blank=True)
    email      = models.EmailField()
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    active_ind = models.BooleanField(default=True)

class Application(models.Model):
    student_id         = models.ForeignKey(Teacher, related_name="applications")
    event_id           = models.ForeignKey(Event, related_name="applications")
    creation_datetime  = models.DateTimeField()
    motivation         = models.TextField(null=True, blank=True)
    special_motivation = models.TextField(blank=True, null=True, blank=True)
    referral_source_id = models.ForeignKey(ReferralSource, related_name="applications")
    teacher_id         = models.ForeignKey(Teacher, related_name="student_applications", null=True)
    status_id          = models.ForeignKey(Status)
    status_reviewer_id = models.ForeignKey(Reviewer, related_name="applications_reviewed")
    completed          = models.BooleanField(default=False)
    email_sent         = models.BooleanField(default=False)
    rsvped             = models.BooleanField(default=False)
    active_ind         = models.BooleanField(default=True)

class Event(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime   = models.DateTimeField()
    location_id    = models.ForeignKey(Location, related_name="events")
    url            = models.URLField(max_length=100)
    active_ind     = models.BooleanField(default=True)

class Status(models.Model):
    description = models.CharField(max_length=100)

class School(models.Model):
    name       = models.CharField(max_length=100)
    region_id  = models.ForeignKey(Region, related_name="schools")
    contact_id = models.ForeignKey(Teacher, related_name="schools")

class ReferralSource(models.Model):
    description = models.CharField(max_length=100)

class Region(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    region_id  = models.ForeignKey(Region, related_name="locations")
    address    = models.CharField(max_length=100)

# TODO: login
class Reviewer(models.Model):
    name              = models.CharField(max_length=30)
    email             = models.EmailField()
    admin             = models.BooleanField(default=False)
    event_admin_id    = models.ManyToManyField(Event, related_name="admins")
    event_reviewer_id = models.ManyToManyField(Event, related_name="reviewers")

class Review(models.Model):
    application_id    = models.ForeignKey(Application, related_name="reviews")
    event_id          = models.ForeignKey(Event, related_name="reviews")
    creation_datetime = models.DateTimeField()
    reviewer_id       = models.ForeignKey(Reviewer, related_name="reviews")
    status_id         = models.ForeignKey(Status, null=True, blank=True)
    comment           = models.TextField(null=True, blank=True)
    rating            = models.IntegerField(null=True, blank=True)
