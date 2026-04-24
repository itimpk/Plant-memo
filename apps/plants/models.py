from django.db import models
from django.contrib.auth.models import User
import uuid
import os

# Create your models here.
def upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]  # get extension e.g. .jpg
    random_name = uuid.uuid4().hex       # random string e.g. a3f92b1c...
    return f'plants/user_{instance.user.id}/{random_name}{ext}'

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    variety = models.CharField(max_length = 100)
    plant_date = models.DateField()
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    group = models.ForeignKey(Group,on_delete= models.CASCADE)

    def __str__(self):
        return self.name
    
class PlantLog(models.Model):
    ACTION_CHOICES = [
        ('water', 'Watering'),
        ('feed', 'Fertilizing'),
        ('prune', 'Pruning'),
        ('note', 'General Note'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} on {self.plant.name}"