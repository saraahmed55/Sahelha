from django.db import models

# Create your models here.
class tracksapp(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=25)  
          
    def __str__(self):
        return self.name