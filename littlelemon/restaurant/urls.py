from django.contrib import admin
from django.urls import path
#from .views import sayHello 
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:id>', views.SingleMenuItemView.as_view()),    
]
