from django.urls import path

# from tweetpost import views
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    
    path('service/',views.Service.as_view(),name='service'),
    
    path('service-details/',views.ServiceDetails.as_view(),name='service-details'),
    
    path('about-us/',views.AboutUs.as_view(),name='about-us'),
    
    path('contact-us/',views.ContactUs.as_view(),name='contact-us'),
    
    path('portfolio/',views.Portfolio.as_view(),name='portfolio'),
    
    path('team/',views.Team.as_view(),name='team'),
    
    path('blog-main/',views.BlogMain.as_view(),name='blog-main'),
    
    path('blog-left-sidebar/',views.BlogLeft.as_view(),name='blog-left-sidebar'),
    
    path('blog-details/',views.BlogDetails.as_view(),name='blog-details'),
    
]