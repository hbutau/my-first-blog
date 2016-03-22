from django.conf.urls import url, patterns
from . import views
from blog.views import (HomeView, Post_ListView, ContactView, GalleryView,
                        EventsView, PythonView, DjangoView, AboutView,
                        ThankYouView, Post_DetailView, ProjectsView,
                        Project_DetailView, Python_DetailView, Django_DetailView)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post_list/', Post_ListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', Post_DetailView.as_view(), name='post_detail'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^events/', EventsView.as_view(), name='events'),
    url(r'^projects/$', ProjectsView.as_view(), name='projects'),
    url(r'^project/(?P<pk>\d+)/$', Project_DetailView.as_view(), name='project_details'),
    url(r'^python/$', PythonView.as_view(), name='python'),
    url(r'^pythonarticle/(?P<pk>\d+)/$', Python_DetailView.as_view(), name='python_details'),
    url(r'^django/$', DjangoView.as_view(), name='django'),
    url(r'^djangoarticle/(?P<pk>\d+)/$', Django_DetailView.as_view(), name='django_details'),
    url(r'^thankyou$', ThankYouView.as_view(), name='thankyou'),
    ]
