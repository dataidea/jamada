from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=222)
    email = models.CharField(max_length=222)
    phone = models.CharField(max_length=222)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class DisplayPicture(models.Model):
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.image.url


