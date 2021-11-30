from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

# Authentication imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Authorization imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# import models
from .models import Skill, Project


# Create your views here.

class Home(TemplateView):
  template_name = "home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["signup_form"] = UserCreationForm()
    context["login_form"] = AuthenticationForm()
    return context
  
class Login(TemplateView):
  template_name = "registration/login.html"

class Signup(TemplateView):
  def get(self, request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)

  def post(self, request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("update-profile")
    else:
      context = {"form": form}
      return render(request, "registration/signup.html", context)

class Profile(TemplateView):
  template_name = "profile.html"

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get("name")
    if name != None:
      context[""]

class Update_Profile(TemplateView):
  template_name = "update_profile.html"

class ProjectCreate(CreateView):
  model = Project
  fields = ['title', 'img', 'collaborators', 'location', 'about', 'skills_needed', 'skills_teachable', 'project_owner']
  template_name = "project_create.html"
  success_url = "/project/"

class Project(TemplateView):
  template_name = "project.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["signup_form"] = UserCreationForm()
    context["login_form"] = AuthenticationForm()
    return context

class Update_Project(TemplateView):
  template_name = "update_project.html"

class SkillList(TemplateView):
  template_name = "skill_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["skills"] = Skill.objects.all()
    return context

class About(TemplateView):
  template_name = "about.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["signup_form"] = UserCreationForm()
    context["login_form"] = AuthenticationForm()
    return context

class About_Dev(TemplateView):
  template_name = "about-dev.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["signup_form"] = UserCreationForm()
    context["login_form"] = AuthenticationForm()
    return context

