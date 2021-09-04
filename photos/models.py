from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self): 
        '''
        Method that saves the Location object
        '''
        self.save()
    
    @classmethod
    def get_location_by_id(cls, location_id):
        '''
        Method that fetches a location based by id
        '''
        return cls.objects.filter(pk = location_id)

    @classmethod
    def update_location(cls, location_id, update_value):
        '''
        Method that Updates a location
        '''
        location = cls.objects.filter(pk = location_id).update(name=update_value)
        



    # Editor.objects.filter(id = 2).update(first_name ='Kim')

    def __str__(self):
        '''
        Method that returns the string representation for the Location Model
        '''
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'gallery/')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_gallery(self):
        gallery = cls.objects.all()
        return gallery
        
    def __str__(self):
        return self.name