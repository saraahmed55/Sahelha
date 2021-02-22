from django.contrib import admin
from .models import courses

# Register your models here.
from .models import tracksapp,Category,courses

admin.site.register(tracksapp)
admin.site.register(Category)
admin.site.register(courses)

