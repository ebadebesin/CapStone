from django.contrib import admin
from django.urls import path
#from .views import sayHello 
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('', sayHello, name='sayHello'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # path('reservations/', views.reservations, name="reservations"),
    path('bookings/', views.bookings, name='bookings'),

    path('index/', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(),  name="menu"),
    path('menu/<int:id>', views.SingleMenuItemView.as_view(),  name="menu_item"),
    # path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('api-token-auth/', obtain_auth_token),    
]
