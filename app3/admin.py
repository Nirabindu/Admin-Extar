from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # fields = ("product_name",)
    list_display = (
        "cat_name","slug"
    )
    ordering = ['cat_name']
    prepopulated_fields = {"slug": ("cat_name",)}
    readonly_fields = ('slug',)

admin.site.register(Category,CategoryAdmin)




# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name",'category')
    # search_fields = ['product_name']
    search_fields = ['product_name','category__cat_name']
    list_display_links = ('category',)
    # view_on_site = False
    # list_select_related = ['category','product']
    # list_select_related =False

    
    # def queryset(self,request):
    #     return super(ProductAdmin,self).queryset(request).select_related('category')
    
#     When value is True, select_related() will always be called. When value is set to False, Django will
# look at list_display and call select_related() if any ForeignKey is present.
    
    
admin.site.register(Product,ProductAdmin )

