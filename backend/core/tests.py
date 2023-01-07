from . models import Locations
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status



class LocationsTestCase(APITestCase):

    """
    Test suite for Locations
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Haoran Xu",
            "message": "Exley Science Center",
            "latitude": "test",
            "longitude": "test",
            "email": "haoranxu@test.com"
        }
        self.url = "/contact/"

    def test_create_location(self):
        '''
        test LocationsViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Locations.objects.count(), 1)
        self.assertEqual(Locations.objects.get().title, "Haoran Xu")

    def test_create_location_without_name(self):
        '''
        test LocationsViewSet create method when name is not in data
        '''
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_location_when_name_equals_blank(self):
        '''
        test LocationsViewSet create method when name is blank
        '''
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_location_without_message(self):
        '''
        test LocationViewSet create method when message is not in data
        '''
        data = self.data
        data.pop("message")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_location_when_message_equals_blank(self):
        '''
        test LocationViewSet create method when message is blank
        '''
        data = self.data
        data["message"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_location_without_email(self):
        '''
        test LocationViewSet create method when email is not in data
        '''
        data = self.data
        data.pop("email")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_location_when_email_equals_blank(self):
        '''
        test LocationViewSet create method when email is blank
        '''
        data = self.data
        data["email"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_location_when_email_equals_non_email(self):
        '''
        test LocationViewSet create method when email is not email
        '''
        data = self.data
        data["email"] = "test"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)