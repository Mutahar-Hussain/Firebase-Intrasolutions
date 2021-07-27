from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from pyrebase.pyrebase import Auth, Database
# Create your views here.
config = {
    "apiKey": "AIzaSyAJpCdlwIlb7uuWyWmQj7A2i9LMwHx4Z6A",
    "authDomain": "first-django-50037.firebaseapp.com",
    "projectId": "first-django-50037",
    "storageBucket": "first-django-50037.appspot.com",
    "messagingSenderId": "460900321469",
    "appId": "1:460900321469:web:13a1bf04c0c018ec9bcfd4",
    "measurementId": "G-JX9CMTVLJ5",
    "databaseURL": "https://first-django-50037-default-rtdb.firebaseio.com",
  }
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def say_hello(request):
   name = database.child('Student').child('name').get().val()
   print(name)
   return render(request, 'index.html', {'name': name})
