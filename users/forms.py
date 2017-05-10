#-*- coding: utf-8 -*-

from django import forms

from TriggerWarnings import trigger_types

class LoginForm(forms.Form):
    userid = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

class ProfileForm(forms.Form):
    error_css_class = ''
    userid = forms.CharField(max_length=100,
                             help_text="Keep it under 100 characters")
    password = forms.CharField(max_length=100,
                               help_text="Keep it under 100 characters")
    confirm_password = forms.CharField(max_length=100,
                                    help_text="Keep it under 100 characters")
    for trigger, descr in trigger_types.types:
        locals()[trigger] = forms.BooleanField(required=False)

    del locals()['trigger']

    #Make sure passowrds match
    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirm_password")
        if p1 != p2:
            raise forms.ValidationError("Passwords did not match!")
