from typing import Any
from django.db import models

# Create your models here.
class post(models.Model):
    title= models.CharField(max_length = 200)
    text= models.TextField()
    author=models.ForeignKey(to='self', on_delete=models.CASCADE)
    create_date=models.DateTimeField()
    Published_date=models.DateTimeField()