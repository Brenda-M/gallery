from django.db import models

class Image(models.Model):
  photo = models.ImageField(upload_to = 'projects/')
  img_name = models.CharField(max_length=100, blank=True)
  description = models.CharField(max_length=150)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.img_name

class Location(models.Model):
  locale = models.CharField(max_length=20)

  def __str__(self):
    return self.locale

class Category(models.Model):
  cat_name = models.CharField(max_length=50)

  def __str__(self):
    return self.cat_name





