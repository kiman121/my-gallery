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