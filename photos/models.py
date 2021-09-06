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
        return cls.objects.filter(id=location_id).first()
    
    @classmethod
    def get_locations_by_id(cls, location_id):
        '''
        Method that fetches a location based by id
        '''
        return cls.objects.filter(id=location_id)

    @classmethod
    def update_location(cls, location_id, update_value):
        '''
        Method that Updates a location
        '''
        location = cls.objects.filter(pk=location_id).update(name=update_value)

    def __str__(self):
        '''
        Method that returns the string representation for the Location Model
        '''
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        '''
        Method that saves the Category object
        '''
        self.save()

    @classmethod
    def get_categories(cls):
        '''
        Method that get all categories
        '''
        categories = cls.objects.all()
        return categories

    @classmethod
    def get_category_by_id(cls, category_id):
        '''
        Method that fetches a category based by id
        '''
        return cls.objects.filter(id=category_id).first()
    
    @classmethod
    def get_categories_by_id(cls, category_id):
        '''
        Method that fetches a category based by id
        '''
        return cls.objects.filter(id=category_id)

    @classmethod
    def search_category(cls, search_term):
        '''
        Method that retrieves a category by provided search term
        '''
        return cls.objects.get(name__icontains=search_term)

    @classmethod
    def update_category(cls, record_id, update_value):
        '''
        Method that Updates a location
        '''
        location = cls.objects.filter(pk=record_id).update(name=update_value)


    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_gallery(cls):
        '''
        Method that fetches all images/photos
        '''
        gallery = cls.objects.all()

        return gallery

    @classmethod
    def get_category_gallery(cls, category):
        '''
        Method that fetches all images/photos (gallery) by category
        '''
        gallery = cls.objects.filter(category=category)

        return gallery

    @classmethod
    def get_location_gallery(cls, location):
        '''
        Method that fetches all images/photos (gallery) by location
        '''
        gallery = cls.objects.filter(location=location)

        return gallery

    @classmethod
    def search_gallery(cls, category):
        '''
        Method that searches images/photos (gallery) by a term
        '''
        # match_category = Category.search_category(search_term).id

        return cls.objects.filter(category=category)

    @classmethod
    def get_gallery_item(cls, id):
        '''
        Method that fetches an image/photo (gallery item) by id
        '''
        photo = cls.objects.get(id=id);
        
        return photo

    def __str__(self):
        '''
        Method that gives the string representation for the Image model
        '''
        return self.name
