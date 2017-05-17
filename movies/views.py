# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from movies.models import Movies
from users.models import Profiles
from TriggerWarnings import trigger_types

# Create your views here.

def search(request):
    results = []

    #Is user logged in?
    if request.session.has_key('userid'):
        u = request.session['userid']

        #Was this a POST?
        #I know I should actually create a Form to handle this input
        #so that it gets cleaned and validated, but this is just some
        #quick prototyping.

        #In order to add ease support for accepting an empty string
        #in the form input:
        # first check if this is a post
        # and then get the movie_title,
        # if empty, simply get all the movies,
        # otherwise do as below.

        if request.POST.get('movie_title'):
            #Case-insensitive search, using "like" matching
            movies = Movies.objects.filter(title__icontains=request.POST.get("movie_title"))
            #Did we find a match?
            if movies.exists():
                #Get the user info (userid are unique so we know that we 
                #will only get back a single result/match).
                user = Profiles.objects.get(userid=u)
                #Check if any returned title meets criteria
                for movie in movies:
                    verdict = "OK"
                    for trigger,descr in trigger_types.types:
#                        if getattr(movie,trigger) == True:
                        if getattr(user,trigger) == True and getattr(user,trigger) == getattr(movie,trigger):
                            verdict = "Not OK"

                    results.append("%s -- %s"%(movie.title,verdict))

        return render(request, 'main.html', {'userid':u, "results":results})
    else:
        return render(request, "login.html", {})

