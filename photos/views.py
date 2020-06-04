from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category

def home(request):

  all_images = Image.objects.order_by('-id').all()
  

  context = {
    'images':all_images
  }

  return render(request, 'photos/home.html', context)

def categories(request):

  title = Categories

  all_categories = Category.objects.all()

  context = {
    'categories':all_categories,
    'title': title
  }

  return render(request, 'photos/categories.html', context)

# def details(request):
#   return render(request, 'photos/details.html')