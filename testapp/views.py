from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'testapp/home.html'

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