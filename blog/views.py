from __future__ import absolute_import
from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime

from blog.forms import ContactForm


class HomeView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['year'] = datetime.now().year
        return context


class Post_ListView(TemplateView):
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = super(Post_ListView, self).get_context_data(**kwargs)
        context['title'] = 'Blog Posts'
        context['year'] = datetime.now().year
        return context


class ContactView(TemplateView):
    contact_form = ContactForm()
    template_name = "blog/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        contact_form = ContactForm()
        context['contact_form'] = contact_form
        context['title'] = 'Contact Us'
        context['message'] = 'Our Contact Details'
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        contact_form = ContactForm(request.POST)
        contact_form.save()

        to = ['anna@anntele.com']
        subject = request.POST.get('subject', '')
        details = request.POST.get('message', '')
        email = request.POST.get('email', '')
        phone =  request.POST.get('phone')
        name = request.POST.get('name')

        ctx = {'name': name,
               'phone': phone,
               'email': email,
               'details': details,
               }

        if subject and details and email:
            try:
                message = render_to_string('emails/webenquiry.txt', ctx)
                EmailMessage(subject, message, to=to).send()
                return HttpResponseRedirect('thankyou')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')


class GalleryView(TemplateView):
    template_name = "blog/gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['title'] = 'My Work in Pictures'
        context['year'] = datetime.now().year
        return context
