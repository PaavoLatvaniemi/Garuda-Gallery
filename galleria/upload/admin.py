from django.contrib import admin
from .models import Photo, PhotoGroup

# Register your models here.
admin.site.register(Photo)
admin.site.register(PhotoGroup)