#-*- coding: utf-8 -*-

from django import forms

from TriggerWarnings import trigger_types

from users.models import Profiles

class LoginForm(forms.Form):
    userid = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

    #Authenicate the user
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        u = self.cleaned_data.get("userid")
        user_check = Profiles.objects.filter(userid=u)
        #If userid doesn't exist, ValidationError
        if not user_check:
            raise forms.ValidationError("Just for testing: userid does not exist.")
        #Check password
        p = self.cleaned_data.get("password")
        if p != Profiles.objects.get(userid=user_check).password:
            raise forms.ValidationError("Just for testing: password was wrong.")
        return cleaned_data


class ProfileForm(forms.Form):
    userid = forms.CharField(max_length=100,
                             help_text="Keep it under 100 characters")
    password = forms.CharField(max_length=100,
                               help_text="Keep it under 100 characters")
    confirm_password = forms.CharField(max_length=100,
                                    help_text="Keep it under 100 characters")
    for trigger, descr in trigger_types.types:
        locals()[trigger] = forms.BooleanField(required=False)

    del locals()['trigger']

    #Make sure userid is not already claimed
    def clean_userid(self):
        new_userid = self.cleaned_data.get("userid")
        existing_user = Profiles.objects.filter(userid=new_userid)
        if existing_user:
            raise forms.ValidationError("That userid is already being used.")
        return new_userid

    #Make sure passowrds match
    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirm_password")
        if p1 != p2:
            raise forms.ValidationError("Passwords did not match!")
        return cleaned_data
