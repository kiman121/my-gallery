from django.test import TestCase
from .models import Location, Category, Image
from django.contrib.auth.models import User
# Create your tests here.


class LocationTestCase(TestCase):
    '''
    Test class for the Location module
    '''
    def setUp(self):
        '''
        Method that creates an instance of the Location class before every test
        '''
        self.new_location = Location(name='Kitale')

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_location, Location))
    
    def test_save_method(self):
        '''
        Test case that confirms that the Location object is being saved
        '''
        self.new_location.save_location()
        my_locations = Location.objects.all()
        self.assertTrue(len(my_locations) > 0)
    
    def test_get_location_by_id(self):
        '''
        Test case that confirms if location is fetched by id
        '''
        self.new_location.save_location()
        record_id = Location.objects.last().id
        my_location = Location.get_locations_by_id(record_id)
        self.assertTrue(len(my_location) > 0)

    def test_update_method(self):
        '''
        Test case that confirms if the update_location method updates a location
        '''
        self.new_location.save_location()
        record_id = Location.objects.last().id
        Location.update_location(record_id, 'Nairobi')
        my_location = Location.objects.get(pk=record_id)

        self.assertEqual(my_location.name, 'Nairobi')
    
    def test_delete_method(self):
        '''
        Test case that confirms if the delete_location method deletes a location
        '''
        self.new_location.save_location()
        record_id = Location.objects.last().id
        Location.delete_location(record_id)

        my_locations = Location.objects.all()
        self.assertTrue(len(my_locations) == 0)

class CategoryTestCase(TestCase):
    '''
    Test class for the Category module
    '''
    def setUp(self):
        '''
        Method that creates an instance of the Category class before every test
        '''
        self.new_category = Category(name='Travel')
    
    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_category, Category))
    
    def test_save_method(self):
        '''
        Test case that confirms that the Category object is being saved
        '''
        self.new_category.save_category()
        my_categories = Category.get_categories()
        self.assertTrue(len(my_categories) > 0)

    def test_get_category_by_id(self):
        self.new_category.save_category()
        record_id = Category.objects.last().id
        my_category = Category.get_categories_by_id(record_id)
        self.assertTrue(len(my_category) > 0)

    def test_update_method(self):
        '''
        Test case that confirms if the update_category method updates a category
        '''
        self.new_category.save_category()
        record_id = Category.objects.last().id
        Category.update_category(record_id, 'Food')
        my_category = Category.objects.get(pk=record_id)

        self.assertEqual(my_category.name, 'Food')

    def test_delete_method(self):
        '''
        Test case that confirms if the delete_category method deletes a category
        '''
        self.new_category.save_category()
        record_id = Category.objects.last().id
        Category.delete_category(record_id)

        my_categories = Category.objects.all()
        self.assertTrue(len(my_categories) == 0)

class ImageTestCase(TestCase):
    '''
    Test class for the Image module
    '''
    def setUp(self):
        '''
        Method that creates the instance of the Image class before every test
        '''
        # Save location
        self.new_location = Location(name='Kitale')
        self.new_location.save_location()
        # Save category
        self.new_category = Category(name='Travel')
        self.new_category.save_category()

        self.new_user = User(first_name = 'James', last_name = 'Bond', username = 'jamie', email = 'jamesbond@gmail.com')
        self.new_user.save()
        # Save Image
        self.new_image = Image(name="East Africa's Delicay", description="The eastern shores have the most teasty...", image="gallery/crying_stone.jpeg", user=self.new_user, 
        location=self.new_location, category=self.new_category,created_at='2021-09-04 20:28:07+03')   
    
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_method(self):
        '''
        Test case that confirms that the Category object is being saved
        '''
        self.new_image.save_image()
        my_images = Image.get_gallery()
        self.assertTrue(len(my_images) > 0)
    
    def test_update_method(self):
        '''
        Test case that confirms if the update_image method updates an image record (name attribute)
        '''
        self.new_image.save_image()
        record_id = Image.objects.last().id
        Image.update_image(record_id, "East Africa's Cuisine")
        my_image = Image.objects.get(pk=record_id)

        self.assertEqual(my_image.name, "East Africa's Cuisine")
    
    def test_delete_method(self):
        '''
        Test case that confirms if the delete_image method deletes a image
        '''
        self.new_image.save_image()
        record_id = Image.objects.last().id
        Image.delete_image(record_id)

        my_images = Image.objects.all()
        self.assertTrue(len(my_images) == 0)