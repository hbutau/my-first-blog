from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)
    slug = AutoSlugField(populate_from='title')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField("full name", max_length=120)
    phone = models.CharField("phone number", max_length=30)
    email = models.CharField("email address", max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    emaildate = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField("full name", max_length=120)
    email = models.CharField("email address", max_length=120)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)
    post = models.CharField(max_length=5)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Event(models.Model):
    name = models.CharField(max_length=200)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    location =  models.CharField(max_length=200)
    website = models.TextField()
    comments = models.TextField()
    dateposted = models.DateTimeField()

    class Meta:
        managed = True

    def __str__(self):
        return self.name
