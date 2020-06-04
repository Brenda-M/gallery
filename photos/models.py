from django.db import models

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

  def __str__(self):
    return self.img_name
  
  def save_image(self):
    return self.save()






