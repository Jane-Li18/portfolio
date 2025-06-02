from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

def main(request):
    return render(request, 'profile/main.html')

def feedback(request):
    return render(request, 'profile/feedback.html')

def static_test(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'vercel_final_test.txt')
    return FileResponse(open(file_path, 'rb'))
