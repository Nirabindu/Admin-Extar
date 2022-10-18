from django.db import models

# Create your models here.
# The admin interface has the ability to edit models on the same page as a parent model. These are called inlines. 



class Author(models.Model):
    author  = models.CharField(max_length = 100)
    
class Book(models.Model):
    author  = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    
    
    
class Person(models.Model):
    name = models.CharField(max_length = 100)
    
class Friendship(models.Model):
    from_person = models.ForeignKey(Person,on_delete = models.CASCADE,related_name="friends")
    to_person = models.ForeignKey(Person, on_delete = models.CASCADE,related_name="from_friends")



class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, related_name='groups')
    
    
    
    
# We can create manually third table for many to many fields 
# class Person(models.Model):
#     name = models.CharField(max_length=128)
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)