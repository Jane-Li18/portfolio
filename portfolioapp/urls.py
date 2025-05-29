from django.urls import path
from .views import main, feedback

urlpatterns = [
    path('', main, name='main'),
    path('feedback/', feedback, name='feedback'),
]
