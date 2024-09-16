

# Create your models here.
from django.db import models

class WorkBoard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    workboard = models.ForeignKey(WorkBoard, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
