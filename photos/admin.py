from django.contrib import admin
from photos.models import Image, Category, Location
# Register your models here.
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)