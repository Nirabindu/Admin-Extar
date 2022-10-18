from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import *
from django.contrib.auth import get_permission_codename
# Register your models here.

# method 1
# adding action method 
# @admin.action(description='Mark selected Articles as published')
# def make_published(modeladmin, request, queryset):
#     queryset.update(status = 'p')

# @admin.action(description='Mark selected Articles as Withdrawn')
# def make_withdrawn(modeladmin, request, queryset):
#     queryset.update(status = 'w')
    

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']
#     ordering = ['title']
#     actions = [make_published,make_withdrawn]
    
    
# admin.site.register(Article, ArticleAdmin)

'''
The example above shows the make_published action defined as a function. That's perfectly fine, but it'
s not perfect from a code design point of view: since the action is tightly coupled to the Article object, it
makes sense to hook the action to the ArticleAdmin object itself.

'''
# method 2

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    list_filter = ['status']
    actions = ['make_published','make_withdrawn']
    
    
    
    '''
    get cation can be given action as per user/ user role etc
    
    '''
    
    def get_actions(self, request):
        actions = super(ArticleAdmin,self).get_actions(request)
        if request.user.username.upper() == 'NILU':
            if 'make_withdrawn' in actions:
                del actions['make_withdrawn']
        return actions
        # if 'delete_selected' in actions:
        # del actions['delete_selected']
        # return actions
        
    

    @admin.action(description='Mark selected stories as published',permissions=['view'])
    def make_published(self,request,queryset):
        update = queryset.update(status = 'p' )
        # update return the number of objects were updates
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            update,
        ) % update, messages.SUCCESS)

    # def has_publish_permission(self,request):
    #     '''
    #     does the user have the publish permission
    #     i dont understand this part
    #     '''
    #     opts = self.opts
    #     codename = get_permission_codename('publish',opts)
    #     return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    
    @admin.action(description='Mark selected stories as Withdrawn')
    def make_withdrawn(self,request,queryset):
        update = queryset.update(status = 'w' )
        '''
        provide msg to the user as per action
        '''
        self.message_user(request, ngettext(
            '%d story was successfully marked as Withdrawn.',
            '%d stories were successfully marked as Withdrawn.',
            update,
        ) % update, messages.SUCCESS)
    

admin.site.register(Article, ArticleAdmin)



# page 973 6.5 not understand