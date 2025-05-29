from django.shortcuts import render 
from django.db import models

def main(request):
    return render(request, 'profile/main.html')

def feedback(request):
    return render(request, 'profile/feedback.html')