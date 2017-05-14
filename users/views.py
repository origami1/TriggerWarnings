# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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

# Start here ... if already logged in, proceed to main, else
# go to login page.
def start(request):
    if request.GET.get('logout', "0") == "1":
        try:
            del request.session['userid']
        except:
            pass

    if request.session.has_key('userid'):
        u = request.session['userid']
        return render(request, 'main.html', {'userid':u})
    else:
        return render(request, 'login.html', {})

# Login page
def login(request):
    userid = "not logged in"

    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)

        #This also checks the credentials
        if MyLoginForm.is_valid():
            userid = MyLoginForm.cleaned_data['userid']
            #Save a session cookie. (Note: this should be accompanied by
            #a corresponding "time value" so that we could expire the
            #cookie w/o waiting on the user to "logout")
            request.session['userid'] = userid
            return render(request, 'main.html', {'userid':userid})

    else:
        if request.session.has_key('userid'):
            u = request.session['userid']
            return render(request, 'main.html', {'userid':u})

    return render(request, 'login.html', {})

# Create profile page
def register(request):
    userid = "_none"
    form_errors = {}

    if request.session.has_key('userid'):
        u = request.session['userid']
        return render(request, 'main.html', {'userid':u})

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


#Logout
def logout(request):
    try:
        del request.session['userid']
    except:
        pass
    return render(request, 'logout.html', {})

