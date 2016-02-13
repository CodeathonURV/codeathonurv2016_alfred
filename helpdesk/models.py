from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime

STATUS_OPTIONS = (
    ("OPEN", "Open"),
    ("CLOSED", "Closed"),
    ("RESPONDED", "Responded")
)

PRIORITY_OPTIONS = (
    ("LOW", "Low"),
    ("MEDIUM", "Medium"),
    ("HIGH", "High")
)

class Department(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Subject(models.Model):
    title = models.CharField(max_length=200)
    year = models.DateTimeField('date_published', default=datetime.now)
    def __unicode__(self):
        return self.title + str(self.year)

class Student(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                          blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    subjects = models.ManyToManyField(Subject, blank=True)
    def __unicode__(self):
        return self.user.username

class Pdi(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                          blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    subjects = models.ManyToManyField(Subject, blank=True)
    office = models.CharField(max_length=200)
    knowledge_area = models.CharField(max_length=200)
    def __unicode__(self):
        return self.user.username

class Pas(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                          blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    task = models.CharField(max_length=200)
    department = models.ForeignKey(Department)
    def __unicode__(self):
        return self.user.username

class Topic(models.Model):
    #It would be interesting to add tags http://django-taggit.readthedocs.org/en/latest/
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_author')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_receiver')
    status = models.CharField(max_length=9, choices=STATUS_OPTIONS, default="OPEN")
    creation_date = models.DateTimeField('date_published', default=datetime.now)
    last_update = models.DateTimeField('last_update', default=datetime.now)
    priority = models.CharField(max_length=9, choices=PRIORITY_OPTIONS, default="MEDIUM")
    is_public = models.BooleanField(default=False)
    content = models.TextField()
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comment_topic')
    date_published = models.DateTimeField('date_published', default=datetime.now)
    def __unicode__(self):
        return self.content
