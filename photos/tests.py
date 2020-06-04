from django.test import TestCase
from .models import Image, Location, Category

class ImageTestClass(TestCase):

  def setUp(self):
    self.category = Category(cat_name='food')
    self.category.save()

    self.location = Location(city='nairobi', country='kenya', locale='westlands')
    self.location.save()

    self.image1 = Image(photo='test.jpg', img_name='test trip', description='short trip to jamaica', location=self.location, category=self.category)
    self.image1.save()
  
  def test_instance(self):
    self.assertTrue(isinstance(self.image1, Image))

  def test_save(self):
    self.image1.save_image()
  
  def test_delete_image(self):
    image2 = Image(photo='test_2.jpg', img_name='test 2 trip', description='short trip to hawaii', location=self.location, category=self.category)
    image2.save_image()
    img_del = Image.objects.filter(id=1)
    all_imgs = Image.objects.all()
    img_del.delete()
    self.assertTrue(len(all_imgs) == 0)
  

    