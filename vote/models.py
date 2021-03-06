from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator

# Create your models here.
class Profile(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-image']

class Projects(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=320)
    link = models.URLField(max_length=60)
    date = models.DateField(auto_now=True)
    screen1 = CloudinaryField('image')
    screen2 = CloudinaryField('image')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        self.name

    @classmethod
    def search_project(cls, word):
        searched = cls.objects.filter(name__icontains = word)
        return searched

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = CASCADE)
    comment = models.TextField(max_length=200)
    pro_id = models.IntegerField(default = 0)

class Votes(models.Model):
    design = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    user = models.ForeignKey(User, on_delete=CASCADE)
    project = models.IntegerField(default=0)