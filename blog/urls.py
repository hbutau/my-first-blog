from django.conf.urls import url, patterns
from . import views
from blog.views import HomeView, Post_ListView, ContactView, GalleryView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post_list/', Post_ListView.as_view(), name='post_list'),
    url(r'^gallery$', GalleryView.as_view(), name='gallery'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    ]
