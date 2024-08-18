from django.contrib import admin

# Register your models here.
from solo.admin import SingletonModelAdmin
# from testapp.models import Blog, BlogItem, HomeSection, Project, ProjectItem, Service, ServiceItem
from testapp.models import BlogTag, HomeSection, Item

@admin.register(HomeSection)
class testapp(admin.ModelAdmin):
    list_display = ['type_choices', 'title','description']


@admin.register(Item)
class testapp(admin.ModelAdmin):
    list_display = ['type', 'title','description']

@admin.register(BlogTag)
class testapp(admin.ModelAdmin):
    list_display = ['tag']





# admin.site.register(ServiceItem)
# admin.site.register(Service)
# admin.site.register(ProjectItem)
# admin.site.register(Project)
# admin.site.register(BlogItem)
# admin.site.register(Blog)