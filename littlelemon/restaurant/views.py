from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# python manage.py migrate books
# python manage.py makemigrations
# for making migrations


#def sayHello(request):
 #return HttpResponse('Hello World')

def index(request):
   return render(request, 'index.html', {})