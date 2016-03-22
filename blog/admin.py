from django.contrib import admin
from .models import (Post, Contact, Comment, Event, Article, AboutPage,
                    DjangoArticle, PythonArticle, Project)

admin.site.register(AboutPage)
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(DjangoArticle)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Project)
admin.site.register(PythonArticle)
