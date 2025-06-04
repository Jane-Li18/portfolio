from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

def main(request):
    return render(request, 'profile/main.html')

def feedback(request):
    return render(request, 'profile/feedback.html')
