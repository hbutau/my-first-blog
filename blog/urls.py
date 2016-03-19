from django.conf.urls import url, patterns
from . import views
from blog.views import (HomeView, Post_ListView, ContactView, GalleryView,
                        EducationView, ProfessionalView, VolunteerView,
                        ThankYouView, Post_DetailView)

import re


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post_list/', Post_ListView.as_view(), name='post_list'),
    url(u'^post/(?P<pk>\d+)/$', Post_DetailView.as_view(), name='post_detail'),
    url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^events', EducationView.as_view(), name='events'),
    url(r'^python$', ProfessionalView.as_view(), name='python'),
    url(r'^django$', VolunteerView.as_view(), name='django'),
    url(r'^thankyou$', ThankYouView.as_view(), name='thankyou'),
    ]
