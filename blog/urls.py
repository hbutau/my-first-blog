from django.conf.urls import url, patterns
from . import views
from blog.views import (HomeView, Post_ListView, ContactView, GalleryView,
                        EducationView, ProfessionalView, VolunteerView,
                        ThankYouView)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post_list/', Post_ListView.as_view(), name='post_list'),
    url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^education', EducationView.as_view(), name='education'),
    url(r'^professional$', ProfessionalView.as_view(), name='professional'),
    url(r'^volunteer$', VolunteerView.as_view(), name='volunteer'),
    url(r'^thankyou$', ThankYouView.as_view(), name='thankyou'),
    ]
