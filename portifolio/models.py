from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    Message = models.TextField(max_length=400)
    Number = models.CharField(max_length=10)


    def __str__(self):
        return (self.name)
