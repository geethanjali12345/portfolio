from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    subject = models.CharField(max_length=255)
    message=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    def __str__(self):
    	return self.name