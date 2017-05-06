from django.conf.urls import url

from . import views

urlpatterns = [
    #landing page (login page)
    url(r'^$', views.index, name='index'),
]
