from django.db import models

class Image(models.Model):
  photo = models.ImageField(upload_to = 'projects/')
  img_name = models.CharField(max_length=100, blank=True)
  description = models.CharField(max_length=150)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

