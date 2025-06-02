from django.urls import path
from .views import main, feedback, static_test

urlpatterns = [
    path('', main, name='main'),
    path('feedback/', feedback, name='feedback'),
    path('static-test/', static_test, name='static-test'),
]
