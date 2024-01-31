from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu
from .models import Booking
from .serializers import MenuSerializer
from .serializers import BookingSerializer

from rest_framework.decorators import api_view
from rest_framework import viewsets
# from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.

# python manage.py migrate 
# python manage.py makemigrations
# for making migrations

def index(request):
   return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id' 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 