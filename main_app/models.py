from django.db import models

from django.db.models import Model
from django.db.models.fields import CharField

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, ManyToManyField

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
  about = models.CharField(max_length=3000)
  skills_current = ManyToManyField(Skill, related_name="users_have")
  skills_learn = ManyToManyField(Skill, related_name="users_learn")

  def __str__(self) -> str:
    return self.user.username

class Project(Model):
  title = CharField(max_length=200)
  img = CharField(max_length=400)
  collaborators = ManyToManyField(User, related_name="projects_collab")
  location = CharField(max_length=50) # Add default to project owner's location
  about = CharField(max_length=5000)
  skills_needed = ManyToManyField(Skill, related_name="projects_required")
  skills_teachable = ManyToManyField(Skill, related_name="projects_teach")
  project_owner = ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

  def __str__(self) -> str:
    return self.title


