from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Menu  
from restaurant.serializers import MenuSerializer



class MenuViewTest(APITestCase):
    def setUp(self):
        # Create test menu instances
        Menu.objects.create(title="Pizza", price=9.99, inventory=10)
        Menu.objects.create(title="Pasta", price=12.99, inventory=8)

    def test_getall(self):
        # Get API response
        response = self.client.get(reverse('menu'))  # Adjust 'menu-list' to your URL name
        # Get data from the database
        menus = Menu.objects.all()
        # Serialize the data
        serializer = MenuSerializer(menus, many=True)
        # Assert
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
