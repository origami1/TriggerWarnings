# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from users.forms import LoginForm

# Create your views here.

# Landing page with login and link to create new profile
def index(request):
    userid = "not logged in"

    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            userid = MyLoginForm.cleaned_data['userid']

    else:
        MyLoginForm = LoginForm()

    return render(request, 'index.html', {'userid' : userid})


def register(request):
    return render(request, "register.html", {})


def login(request):
    userid = "not logged in"

    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            userid = MyLoginForm.cleaned_data['userid']

    else:
        MyLoginForm = LoginForm()


    return render(request, 'loggedin.html', {'userid' : userid})


