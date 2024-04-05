from django.db import models

# Create your models here.
class ToDoApp(models.Model):
    content = models.TextField()