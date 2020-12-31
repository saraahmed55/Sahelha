from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "tracks/%s.%s"%(instance.id, extension)

def image_upload_detail(instance, filename):
    imagename, extension = filename.split(".")
    return "tracks/detail%s.%s"%(instance.id, extension)

class tracksapp(models.Model):

    title=models.CharField(max_length=100)
    description_in_list=models.TextField(max_length=1000)
    description_in_detail=models.TextField(max_length=1000)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    image_in_list = models.ImageField( upload_to=image_upload)
    image_in_detail = models.ImageField( upload_to=image_upload_detail)
    slug= models.SlugField(blank=True, null=True)
    courses=models.ManyToManyField("courses")

    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(tracksapp,self).save(*args, **kwargs)

class courses(models.Model):
    title=models.CharField(max_length=30)
    firstcourse_title=models.CharField(max_length=30, blank=True, null=True)
    firstcourse_url=models.URLField(blank=True, null=True)
    secondcourse_title=models.CharField(max_length=30, blank=True, null=True)
    secondcourse_url=models.URLField(blank=True, null=True)
    thirdcourse_title=models.CharField(max_length=30, blank=True, null=True)
    thirdcourse_url=models.URLField(blank=True, null=True)
    slug=models.SlugField(blank=True, null=True)



    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("tracksapp:track_detail",kwargs={"slug":self.slug})


class Category(models.Model):
    name=models.CharField(max_length=25)  
          
    def __str__(self):
        return self.name





    