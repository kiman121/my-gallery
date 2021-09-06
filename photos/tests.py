from django.test import TestCase
from .models import Location, Category
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
    
    # def tearDown(self):
    #     Location.objects.all().delete()

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
        self.new_location.save_location()
        my_location = Location.get_locations_by_id(1)
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
    
    # def test_delete_method(self):
    #     '''
    #     Test case that confirms if the delete_location method deletes a location
    #     '''
    #     self.new_location.save_location()
    #     # second_location = Location(name="Mombasa")
    #     # second_location.save_location()

    #     # record_id = Location.objects.last().id
    #     Location.delete_location(1)

        # my_locations = Location.objects.all()
        # self.assertTrue(len(my_locations) == 0)
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
        my_category = Category.get_categories_by_id(1)
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
    