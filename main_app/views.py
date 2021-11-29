from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Authentication imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Authorization imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# import models
from .models import Skill


# Create your views here.

class Home(TemplateView):
  template_name = "home.html"
  
class Login(TemplateView):
  template_name = "registration/login.html"

class Signup(TemplateView):
  template_name = "registration/signup.html"

class Profile(TemplateView):
  template_name = "profile.html"

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get("name")
    if name != None:
      context[""]

class Update_Profile(TemplateView):
  template_name = "update_profile.html"

class Project(TemplateView):
  template_name = "project.html"

class About(TemplateView):
  template_name = "about.html"

class About_Dev(TemplateView):
  template_name = "about-dev.html"


