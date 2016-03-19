from django.contrib import admin
from .models import Post, Contact, Comment, Event

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Event)
