from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from datetime import date
from .models import *

# Register your models here.


class EmailFilter(SimpleListFilter):
    """
    custom filter
    Human- readable title which will be displayed in the
    right admin side bar just above the filter options
    """

    title = "Email Filter"
    parameter_name = "email"

    def lookups(self, request, model_admin):
        """
        Return a list of tuples. The first element in each tuple is the
        coded value for the option that will appear in the url query.The
        second elements is the human readable option that appear in the right
        side bar
        """

        return (("having-email", "has_email"), ("not-having-email", "no_email"))

    def queryset(self, request, queryset):

        """
        we have to create two query for has_email
        and for no_email
        """
        if not self.value():
            return queryset
        if self.value().lower() == "having-email":
            return queryset.exclude(email=None)
        if self.value().lower() == "not-having-email":
            return queryset.filter(email=None)


class dobFilter(SimpleListFilter):
    title = " Dob Filter"
    parameter_name = "date_of_birth"

    def lookups(self, request, model_admin):
        """
        Return a list of tuples. The first element in each tuple is the
        coded value for the option that will appear in the url query.The
        second elements is the human readable option that appear in the right
        side bar
        """

        return (
            ("80s", "in the eighties"),
            ("90s", "in the nineties"),
            ("20s", "in the twenties")
        )

    def queryset(self, request, queryset):

        """
        we have to create two query for has_email
        and for no_email
        """
        if not self.value():
            return queryset
        if self.value() == "80s":
            return queryset.filter(
                date_of_birth__gte=date(1980, 1, 1),
                date_of_birth__lte=date(1989, 12, 31),
            )

        if self.value() == "90s":
            return queryset.filter(
                date_of_birth__gte=date(1990, 1, 1),
                date_of_birth__lte=date(1999, 12, 31),
            )
        
        if self.value() == "20s":
            return queryset.filter(
                date_of_birth__gt = date(1999, 12,31),
                date_of_birth__lte = date(2999, 12, 31)
            )


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "date_of_birth",
        "decade_born_in",
        "email",
    )
    list_display_links = ('name',)
    list_editable = ('email',)
    list_filter = (EmailFilter, dobFilter)
    list_per_page = 2


admin.site.register(User, UserAdmin)



class PriceFilter(SimpleListFilter):
    title = " Price Filter"
    parameter_name = "price"


    def lookups(self, request, model_admin):
        return (
            
            ('under-1000','sort by under price 1000'),
            ('under-5000','sort by under price 5000')
            
        )
        
    def queryset(self, request, queryset):
        
        if not self.value():
            return queryset
        
        if self.value() == "under-1000":
            return queryset.filter(
                product_price__lte=1000,
            )
        if self.value() == "under-5000":
            return queryset.filter(
                product_price__lte = 5000,
            )
        

class ProductAdmin(admin.ModelAdmin):
    # fields = ("product_name",)
    list_display = (
        "id",
        "product_name",
        "product_price",
    )
    list_filter = (PriceFilter,)


admin.site.register(ProductCost, ProductAdmin)