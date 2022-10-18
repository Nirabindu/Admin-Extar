from django.contrib import admin
from .models import *

# Register your models here.


class BookInline(admin.StackedInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]


admin.site.register(Author, AuthorAdmin)


# class FriendshipInline(admin.TabularInline):
#     model = Friendship
#     fk_name = "to_person"
# class PersonAdmin(admin.ModelAdmin):
#     inlines = [
#     FriendshipInline,
# ]

# admin.site.register(Person, PersonAdmin)


# this is for third table that django created by default for many to many field
class MembershipInline(admin.TabularInline):
    model = Group.members.through


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ("members",)


admin.site.register(Person,PersonAdmin)
admin.site.register( Group,GroupAdmin)



# admin for our self created many to many field

# class MembershipInline(admin.TabularInline):
#     model = Membership
#     extra = 1
# # This example uses the default InlineModelAdmin values for the Membership model, and limits the extra add
# # forms to one. This could be customized using any of the options available to InlineModelAdmin classes.
# # Now create admin views for the Person and Group models:
# class PersonAdmin(admin.ModelAdmin):
#     inlines = (MembershipInline,)
# class GroupAdmin(admin.ModelAdmin):
#     inlines = (MembershipInline,)
# # Finally, register your Person and Group models with the admin site:
# admin.site.register(Person, PersonAdmin)
# admin.site.register(Group, GroupAdmin)