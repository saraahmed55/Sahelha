from django.contrib import admin

# Register your models here.
from .models import tracksapp,Category,courses

admin.site.register(tracksapp)
admin.site.register(Category)
admin.site.register(courses)