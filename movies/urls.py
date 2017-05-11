from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #landing page (login page)
#    url(r'^$', views.start, name='start'),
#    url(r'^login/', views.login, name='login'),
#    url(r'^register/', views.register, name='register'),
    url(r'^search/', views.search, name='search'),
]
