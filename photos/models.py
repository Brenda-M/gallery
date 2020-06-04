from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Location(models.Model):
  city = models.CharField(max_length=30)
  country = models.CharField(max_length=30)
  locale = models.CharField(max_length=30)


  def __str__(self):
    return self.locale

class Category(models.Model):
  cat_name = models.CharField(max_length=50)

  def __str__(self):
    return self.cat_name


class Image(models.Model):
  photo = models.ImageField(upload_to = 'projects/')
  img_name = models.CharField(max_length=100, blank=True)
  description = models.CharField(max_length=150)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  timestamp = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ['-id']

  def __str__(self):
    return self.img_name
  
  def save_image(self):
    return self.save()
  
  def delete_image(self):
    return self.delete()

  @classmethod
  def by_category(cls, category_name):
    try:
      img_by_category = cls.objects.filter(category= category_name).all()
      return img_by_category
    except ObjectDoesNotExist:
      message = "There are no images from that category"
      return message
  
  @classmethod
  def by_location(cls, place):
    try:
     img_by_location = cls.objects.filter(location=place).all()
     return img_by_location
    except ObjectDoesNotExist:
      message = "There are no images from that location"
      return message
  







