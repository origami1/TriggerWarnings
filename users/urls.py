from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #landing page (login page)
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
]
