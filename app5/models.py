from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length = 100)
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    sub_category_name = models.CharField(max_length = 100)