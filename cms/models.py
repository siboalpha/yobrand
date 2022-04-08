from operator import mod
from turtle import position
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]

    WEB_DESIGNER = 'WEB DESIGNER'
    CONTENT_MANAGER = 'CONTENT CONTENT_MANAGER'
    SOCIAL_MANAGER = 'SOCIAL SOCIAL_MANAGER'
    POSITION_CHOICES = [
        (WEB_DESIGNER, 'WEB DESIGNER'),
        (CONTENT_MANAGER, 'CONTENT MANAGER'),
        (SOCIAL_MANAGER, 'SOCIAL_MANAGER')
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=False)
    birthday = models.DateTimeField(auto_now_add=False)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES, default=MALE)
    position = models.CharField(max_length=40, choices=POSITION_CHOICES, default=WEB_DESIGNER)
    address = models.CharField(max_length=40, null=True)
    address2 = models.CharField(max_length=40, null=True)
    country = models.CharField(max_length=40, null=True)
    state_city = models.CharField(max_length=40, null=True)
    eduction = models.CharField(max_length=40, null=True)



    def __str__(self):
        return self.username.first_name


class Client(models.Model):
    name = models.CharField(max_length=40, null=True)
    website = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    linkedin = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    COMPLETE = 'COMPLETE'
    PENDING = 'PENDING'
    UNCOMPLETE = 'UNCOMPLETE'
    PROJECT_STATUS_CHOICES = [
        (COMPLETE, 'COMPLETE'),
        (PENDING, 'PENDING'),
        (UNCOMPLETE, 'UNCOMPLETE')
    ]

    WEBDESIGN = 'WEBDESIGN'
    CONTENT = 'CONTENT'
    SOCIAL = 'SOCIAL'
    PROJECT_STATUS_CHOICES = [
        (WEBDESIGN, 'COMPLETE'),
        (CONTENT, 'PENDING'),
        (SOCIAL, 'UNCOMPLETE')
    ]
    name = name = models.CharField(max_length=40, null=True)
    description = models.TextField(max_length=200, null=True)
    status = models.CharField(max_length=40, choices=PROJECT_STATUS_CHOICES, default=WEBDESIGN)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField(max_length=40, null=True)
    description = models.TextField(max_length=200, null=True)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL ,null=True)
    complete = models.BooleanField(default=False)
    due_date = models.DateField(auto_now_add=False, null=True)
    due_time = models.TimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.title
    


class Activity(models.Model):
    title = models.CharField(max_length=40, null=True)
    description = models.TextField(max_length=200, null=True)
    due_date = models.DateField(auto_now_add=False, null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title

        
class Request(models.Model):
    title = models.CharField(max_length=100, null=True)
    request_to = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title
