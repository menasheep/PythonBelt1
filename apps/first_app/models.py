# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

# Create your models here.

class UserManager(models.Manager):
    def login(self, postData):
        print "Running a login function!"
        # print "If successful login occurs, maybe return {'theuser':user} where user is a user object?")
        # print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
    def register(self, postData):
        print "Register as a new user here!"
        # print "If successful, maybe return {'theuser':user} where user is a user object?"
        # print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short']")

class User(models.Model):
    name = models.CharField(max_length=45, null=False)
    username = models.CharField(max_length=45, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    confirm_password = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


objects = UserManager()

# username validation
class CustomUser(User): 
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True 

# class models.User:
#     check_password(raw_password)