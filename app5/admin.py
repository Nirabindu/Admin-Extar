from django.contrib import admin
from .models import *
# Register your models here.

'''
this porsena also went to show admin site that is superuser
'''
admin.site.register(Category)



class CategoryAdminArea(admin.AdminSite):
    '''
    diff admin site as per user and model
    '''
    site_header = 'Category Admin Site'
    site_title = "Category Administrator"
    index_title = "CategoryAdminNew"
    
category_admin_site = CategoryAdminArea(name = 'CategoryAdmin')

category_admin_site.register(Category)



# apps.py
# from django.contrib.admin.apps import AdminConfig

# override default admin area to my admin area when we hti /admin this will open by default
# class CategoryAdminConfig(AdminConfig):
#     default_site = 'app.admin.CategoryAdminArea'