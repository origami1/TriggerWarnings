# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from users.forms import LoginForm, ProfileForm
from users.models import Profiles
from TriggerWarnings import trigger_types

# Create your views here.

import logging
logger = logging.getLogger(__name__)
myhandler = logging.StreamHandler()
myformatter = logging.Formatter(fmt="%(levelname)s: %(message)s")
myhandler.setFormatter(myformatter)
logger.addHandler(myhandler)

# Landing page with login and link to create new profile
def index(request):
    userid = "not logged in"

    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)

        #This also checks the credentials
        if MyLoginForm.is_valid():
            userid = MyLoginForm.cleaned_data['userid']
            return render(request, 'main.html', {'userid':userid})

    else:
        MyLoginForm = LoginForm()

    return render(request, 'index.html', {'userid' : userid})


def register(request):
    userid = "_none"
    form_errors = {}

    logger.error("register: enter")

    if request.method == 'POST':
        MyProfileForm = ProfileForm(request.POST)

        if MyProfileForm.is_valid():
            u = MyProfileForm.cleaned_data['userid']
            p = MyProfileForm.cleaned_data['password']
            data_dict = {}
            for trigger,descr in trigger_types.types:
                data_dict[trigger] = MyProfileForm.cleaned_data[trigger]
            profile = Profiles.objects.create(userid=u, password=p, **data_dict)
            return render(request, 'main.html', {'userid':u})
        else:
            userid = "_invalid"
            form_errors = MyProfileForm.errors

    else:
        MyProfileForm = ProfileForm()

    return render(request, 'register.html', {'userid':userid, "trigger_types":trigger_types.types, 'errors':form_errors, 'myform':MyProfileForm})


def login(request):
    userid = "not logged in"

    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            userid = MyLoginForm.cleaned_data['userid']

    else:
        MyLoginForm = LoginForm()


    return render(request, 'loggedin.html', {'userid' : userid})


