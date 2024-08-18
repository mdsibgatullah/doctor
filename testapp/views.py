from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView

from testapp.models import HomeSection, Item

# Create your views here.

class Home(TemplateView):
    template_name = 'testapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero'] = HomeSection.objects.all()[0]
        context['about'] = HomeSection.objects.all()[1]
        context['project'] = HomeSection.objects.all()[2]
        context['client'] = HomeSection.objects.all()[3]
        context['ask'] = HomeSection.objects.all()[4]

        context['service_item'] = Item.objects.filter(type="SERVICE")
        context['project_item'] = Item.objects.filter(type="PROJECT")
        context['blog_item'] = Item.objects.filter(type="BLOG")

        return context

class Service(TemplateView):
    template_name = 'testapp/service.html'

class ServiceDetails(TemplateView):
    template_name = 'testapp/service-details.html'

class AboutUs(TemplateView):
    template_name = 'testapp/about-us.html'

class ContactUs(TemplateView):
    template_name = 'testapp/contact-us.html'

class Portfolio(TemplateView):
    template_name = 'testapp/portfolio.html'

class Team(TemplateView):
    template_name = 'testapp/team.html'

class BlogMain(TemplateView):
    template_name = 'testapp/blog-main.html'

class BlogLeft(TemplateView):
    template_name = 'testapp/blog-left-sidebar.html'

class BlogDetails(TemplateView):
    template_name = 'testapp/blog-details.html'