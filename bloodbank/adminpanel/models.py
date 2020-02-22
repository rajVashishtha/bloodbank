from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100,null=True)
  address = models.TextField(null=True)
  email = models.CharField(max_length=100,null=True)
  password = models.CharField(max_length=100,null=True)
  created_at = models.DateTimeField(default=timezone.now,null=True)
  #model end
