from django.db import models

# Create your models here.


STATUS_ChOICE = [
    
    ('d','Draft'),
    ('p','Published'),
    ('w','Withdrawn'),
    
]


class Article(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    status = models.CharField(max_length = 1, choices = STATUS_ChOICE)
    
    
    def __str__(self) -> str:
        return self.title