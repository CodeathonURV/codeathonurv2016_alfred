#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime

STATUS_OPTIONS = (
    ("OPEN", "Obert"),
    ("CLOSED", "Tancat"),
    ("RESPONDED", "Respost")
)

PRIORITY_OPTIONS = (
    ("LOW", "Baixa"),
    ("MEDIUM", "Mitja"),
    ("HIGH", "Alta")
)

class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nom')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'Departament'
        verbose_name_plural = 'Departaments'

class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name='Nom')
    year = models.DateTimeField('any', default=datetime.now)
    def __unicode__(self):
        return self.title + str(self.year)
    class Meta:
        verbose_name = 'Assignatura'
        verbose_name_plural = 'Assignatures'

class Student(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                          blank=True, verbose_name='Imatge')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    subjects = models.ManyToManyField(Subject, blank=True)
    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Estudiant'
        verbose_name_plural = 'Estudiants'

class Pdi(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                          blank=True, verbose_name='Imatge')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    subjects = models.ManyToManyField(Subject, blank=True)
    office = models.CharField(max_length=200,verbose_name='Despatx')
    knowledge_area = models.CharField(max_length=200, verbose_name='Especialitat')
    def __unicode__(self):
        return self.user.username
    class Meta:
        verbose_name = 'Pdi'
        verbose_name_plural = 'Pdi'

class Pas(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                          blank=True, verbose_name='Imatge')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    task = models.CharField(max_length=200, verbose_name='Tasca')
    department = models.ForeignKey(Department)
    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Pas'
        verbose_name_plural = 'Pas'

class Topic(models.Model):
    #It would be interesting to add tags http://django-taggit.readthedocs.org/en/latest/
    title = models.CharField(max_length=200, verbose_name='Assumpte')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_author', verbose_name='Autor')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_receiver', blank=True,  null=True, verbose_name='Receptor')
    department = models.BooleanField(default=False)
    status = models.CharField(max_length=9, choices=STATUS_OPTIONS, default="OPEN", verbose_name="Estat")
    creation_date = models.DateTimeField('Data de publicació', default=datetime.now)
    last_update = models.DateTimeField('Data actualització', default=datetime.now)
    priority = models.CharField(max_length=9, choices=PRIORITY_OPTIONS, default="MEDIUM", verbose_name='')
    is_public = models.BooleanField(default=False, verbose_name="És public?")
    content = models.TextField()
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultes'

class Comment(models.Model):
    content = models.TextField()
    rating = models.FloatField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comment_topic')
    date_published = models.DateTimeField('Data de publicació', default=datetime.now)
    document = models.FileField(null=True, blank=True)
    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = 'Comentari'
        verbose_name_plural = 'Comentaris'
