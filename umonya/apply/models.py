from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

class School(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name="schools")

class Location(models.Model):
    region = models.ForeignKey(Region, related_name="locations")
    address = models.CharField(max_length=100)

class Event(models.Model):
    datetime = models.DateTimeField()
    location = models.ForeignKey(Location, related_name="events")
    url = models.URLField(max_length=100)

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=36)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(School, related_name="teachers")
    email = models.EmailField()
    concat_no = models.CharField(max_length=20)

class Student(models.Model):
    student_id = models.CharField(max_length=36)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(School, related_name="students")
    alt_event = models.BooleanField()
    grade = models.IntegerField()
    email = models.EmailField()
    contact_no = models.CharField(max_length=20)
    alt_contact_no = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, blank=True)

class ReferralSource(models.Model):
    description = models.CharField(max_length=100)

class Status(models.Model):
    description = models.CharField(max_length=100)

# TODO: login
class Reviewer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    admin = models.BooleanField()
    event_admin = models.ManyToManyField(Event, related_name="admins")
    event_reviewer = models.ManyToManyField(Event, related_name="reviewers")

class Application(models.Model):
    student = models.ForeignKey(Teacher, related_name="applications")
    event = models.ForeignKey(Event, related_name="applications")
    creation_time = models.DateTimeField()
    motivation = models.TextField()
    special_motivation = models.TextField(blank=True)
    referral_source = models.ForeignKey(ReferralSource, related_name="applications")
    teacher = models.ForeignKey(Teacher, related_name="student_applications")
    status = models.ForeignKey(Status)
    status_reviewer = models.ForeignKey(Reviewer, related_name="applications_reviewed")
    completed = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)
    rsvped = models.BooleanField(default=False)

class Review(models.Model):
    application = models.ForeignKey(Application, related_name="reviews")
    event = models.ForeignKey(Event, related_name="reviews")
    creation_time = models.DateTimeField()
    reviewer = models.ForeignKey(Reviewer, related_name="reviews")
    status = models.ForeignKey(Status, blank=True)
    comment = models.TextField(blank=True)
    rating = models.IntegerField(blank=True)
