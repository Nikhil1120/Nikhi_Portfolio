from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    subject=models.CharField(max_length=30)
    message=models.TextField(max_length=100)
    
