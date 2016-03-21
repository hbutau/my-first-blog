from django.conf.urls import url, patterns
from . import views
from blog.views import (HomeView, Post_ListView, ContactView, GalleryView,
                        EventsView, PythonView, DjangoView, AboutView
                        ThankYouView, Post_DetailView)

import re


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post_list/', Post_ListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', Post_DetailView.as_view(), name='post_detail'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^events', EventsView.as_view(), name='events'),
    url(r'^python$', PythonView.as_view(), name='python'),
    url(r'^django$', DjangoView.as_view(), name='django'),
    url(r'^thankyou$', ThankYouView.as_view(), name='thankyou'),
    ]
