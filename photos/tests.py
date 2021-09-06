from django.test import TestCase
from .models import Location
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
    
    def tearDown(self):
        Location.objects.all().delete()

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
        my_location = Location.get_location_by_id(1)
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