from django.contrib import admin

# Register your models here.
from .models import tracksapp,Category

admin.site.register(tracksapp)
admin.site.register(Category)