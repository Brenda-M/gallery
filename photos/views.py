from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category

def home(request):

  all_images = Images.objects.all()

  context = {
    'images':all_images
  }

  return render(request, 'photos/home.html', context)
