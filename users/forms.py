#-*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    userid = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

