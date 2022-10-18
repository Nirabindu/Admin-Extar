from django.db import models
from django.contrib import admin

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(blank = True , null = True)
    email = models.EmailField(unique = True, blank = True, null = True)
    
    
    @admin.display(description='Birth Decade',empty_value='None')
    def decade_born_in(self):
        '''
        we can show an calculated fields in admin from django models
        '''
        try:
            return "%d's" %(self.date_of_birth.year // 10*10)
        except:
            pass
    
    def __str__(self) -> str:
        return self.name


# blank = True  if we not passing data the field will blank only
# null true if are not passing data to fields that will store null



class ProductCost(models.Model):
    
    """
    product cost is use to store cost of a product
    """
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self) -> str:
        return self.product_name