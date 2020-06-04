from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category

def home(request):

  all_images = Image.objects.all()

  context = {
    'images':all_images
  }

  return render(request, 'photos/home.html', context)

def details(request):
  return render(request, 'photos/details.html')
