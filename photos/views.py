import pyperclip
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Location, Category

def home(request):

  all_images = Image.objects.order_by('-id').all()
  

  context = {
    'images':all_images
  }

  return render(request, 'photos/home.html', context)

def categories(request):

  title = 'Categories'

  all_categories = Category.objects.all()

  context = {
    'categories':all_categories,
    'title': title
  }

  return render(request, 'photos/categories.html', context)

def locations(request):

  title = 'Locations'

  all_locations = Location.objects.all()

  context = {
    'locations':all_locations,
    'title': title
  }

  return render(request, 'photos/locations.html', context)

def category_view(request, category_name):

  cat = Image.by_category(category_name)

  # title = f"{}".format(place)

  context = {
    'cat_results': cat
  }

  return render(request, 'photos/category_view.html', context)

def location_view(request, place):

  locale = Image.by_location(place)

  # title = f"{}".format(place)

  context = {
    'loc_results': locale
  }

  return render(request, 'photos/location_view.html', context)

def copy_url(request, pk):

  img = Image.objects.filter(id=pk)

  image_url = img.copy_img_url()

  pyperclip.copy(image_url)

  return HttpResponseRedirect(self.request.path_info)


def search(request):
  template = 'photos/search.html'
  query = request.GET.get('q') #q is the query variable when users searches webite
  results = Image.objects.filter(
    Q(img_name__icontains=query) | 
    Q(description__icontains=query) 
    )
    
  context ={
    'results':results,
    'term':query
  }
  return render(request, template, context)

# def details(request):
#   return render(request, 'photos/details.html')
