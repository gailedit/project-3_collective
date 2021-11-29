from django.db import models

from django.db.models import Model
from django.db.models.fields import CharField

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Skill(Model):
  name = CharField(max_length=50)

  def __str__(self) -> str:
    return self.name

  class Meta:
    ordering = ['name']



class Profile(Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=100)
  image = models.CharField(max_length=400, default="https://static.thenounproject.com/png/4214241-200.png")



class Project(Model):
  title = CharField(max_length=200)
  img = CharField(max_length=400)
  description = CharField(max_length=5000)
  location = CharField(max_length=50) # Add default to project owner's location














# skills = [
#   Skill("Painting"),
#   Skill("Drawing"),
#   Skill("Watercolor"),
#   Skill("Welding"),
#   Skill("Project Management"),
#   Skill("Grant Writing"),
#   Skill("Woodworking"),
#   Skill("LED lights"),
# ]
