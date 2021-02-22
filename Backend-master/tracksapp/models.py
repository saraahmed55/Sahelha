from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "tracks/%s.%s"%(instance.id, extension)

def image_upload_detail(instance, filename):
    imagename, extension = filename.split(".")
    return "tracks/detail%s.%s"%(instance.id, extension)

class tracksapp(models.Model):

    title=models.CharField(max_length=100, verbose_name='Track Name')
    description_in_list=models.TextField(max_length=1000, verbose_name='Description in Home')
    description_in_detail=models.TextField(max_length=1000, verbose_name="Description inside Track's Page")
    category=models.ForeignKey('Category',on_delete=models.CASCADE, verbose_name='Category')
    image_in_list = models.ImageField( upload_to=image_upload, verbose_name='Image in Home')
    background_in_detail = models.ImageField( upload_to=image_upload_detail, verbose_name="Background Image in Track's page")
    slug= models.SlugField(blank=True, null=True)
    courses=models.ManyToManyField('courses')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(tracksapp,self).save(*args, **kwargs)

class courses(models.Model):


    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() 

        options = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )

    title=models.CharField(max_length=30, verbose_name='Courses Name')
    firstcourse_title=models.CharField(max_length=30, blank=True, null=True, verbose_name="First Course Title")
    firstcourse_url=models.URLField(blank=True, null=True, verbose_name="First Course URL")
    secondcourse_title=models.CharField(max_length=30, blank=True, null=True , verbose_name="Second Course Title")
    secondcourse_url=models.URLField(blank=True, null=True, verbose_name="Second Course URL")
    thirdcourse_title=models.CharField(max_length=30, blank=True, null=True, verbose_name="Third Course Title")
    thirdcourse_url=models.URLField(blank=True, null=True, verbose_name="Third Course URL")
    slug=models.SlugField(blank=True, null=True)
    favourites=models.ManyToManyField(
        User,related_name='favourite',default=None,blank=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager


    # class Meta:
    #     ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("tracksapp:track_detail",kwargs={"slug":self.slug})

class Category(models.Model):
    name=models.CharField(max_length=25)  
          
    def __str__(self):
        return self.name   