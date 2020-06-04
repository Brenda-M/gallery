from django.test import TestCase
from .models import Image, Location, Category

class ImageTestClass(TestCase):

  def setUp(self):
    self.category = Category(cat_name='food')
    self.category.save()

    self.location = Location(city='nairobi', country='kenya', locale='westlands')
    self.location.save()

    self.image = Image(photo='test.jpg', img_name='test trip', description='short trip to jamaica', location=self.location, category=self.category)
    self.image.save()
  
  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))

  def test_save(self):
    self.image.save_image()
  
  # def test_delete_image(self):
  #   del_img = Image.object.filter(id=2).delete()

   