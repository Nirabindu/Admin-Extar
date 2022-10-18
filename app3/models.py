from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length = 100)
    slug = models.SlugField(null = True, blank = True)
    
    def __str__(self) -> str:
        return self.cat_name



class Product(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE, related_name = 'product')
    product_name = models.CharField(max_length = 100)
    
    
    def __str__(self) -> str:
        return self.product_name