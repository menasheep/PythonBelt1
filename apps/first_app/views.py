# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.

def main(request):
    return render(request,'first_app/main.html')

def create(request):
    User.objects.create(name='',username='',password='',confirm_password=True)
    user = User.objects.all()
    print "New user has been created!"
    print user
    return render(request,'trav_dash.html')

