from django.contrib import admin
from .models import Post, Contact, Comment, Event, Article

admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Post)
