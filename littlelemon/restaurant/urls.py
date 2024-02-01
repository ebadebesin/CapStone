from django.contrib import admin
from django.urls import path
#from .views import sayHello 
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:id>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),    
]
