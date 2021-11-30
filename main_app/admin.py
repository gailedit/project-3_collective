from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Skill, Project

# Register your models here.

from . import models

admin.site.register(Skill)
admin.site.register(Project)
