from django.db import models
from solo.models import SingletonModel
# Create your models here.
from ckeditor.fields import RichTextField


class HomeSection(models.Model):
    TYPE_CHOICES = (
        ("HERO", "hero"),
        ("ABOUT", "about"),
        ("PROJECT", "project"),
        ("CLIENT", "client"),
        ("ASK-PROJECT", "ask-project"),
    )
    sub_title = models.CharField(max_length = 100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = RichTextField()
    link = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='testapp/', default='image/', null=True, blank=True)
    type_choices = models.CharField(max_length=15,choices=TYPE_CHOICES,default="HERO")
    def __str__(self):
        return self.title
    
#Home all Item ( service, project, blog )
class BlogTag(models.Model):
    tag = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.tag
class Item(models.Model):
    TYPE_CHOICES = (
        ("SERVICE", "service"),
        ("PROJECT", "project"),
        ("BLOG", "blog"),
    )
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='item/image', default='image', null=True, blank=True)
    icon_class = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    blog_tag = models.ManyToManyField(BlogTag, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="SERVICE")
    media = models.CharField(max_length=80, null=True, blank=True)
    def __str__(self):
        return self.title




#service
# class ServiceItem(models.Model):
#     title = models.CharField(max_length=100)
#     description = RichTextField()
#     icon_class = models.CharField(max_length=100)
#     def __str__(self):
#         return self.title

# class Service(SingletonModel):
#     name = models.CharField(max_length=50)
#     service_item = models.ManyToManyField(ServiceItem)

#projects
# class ProjectItem(models.Model):
#     title = models.CharField(max_length=100)
#     description = RichTextField()
#     def __str__(self):
#         return self.title

# class Project(SingletonModel):
#     name = models.CharField(max_length=50)
#     service_item = models.ManyToManyField(ServiceItem)


# #Blog
# class BlogItem(models.Model):
#     title = models.CharField(max_length=100)
#     description = RichTextField()
#     date = models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.title

# class Blog(SingletonModel):
#     name = models.CharField(max_length=50)
#     service_item = models.ManyToManyField(ServiceItem)