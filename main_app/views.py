from django.shortcuts import render, redirect

# import basic views
from django.views import View


from django.forms import ModelForm

# import httpresponse
from django.http import HttpResponse

# import views for templates
from django.views.generic.base import TemplateView

#import detail view
from django.views.generic.detail import DetailView

# import for create, read, update, and delete
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

# Authentication imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Authorization imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# import models
from .models import Skill, Project, Profile


# Create your views here.

# === SECTION Landing Page: auth & no auth ===
class Landing(TemplateView):
  template_name = "landing.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["signup_form"] = UserCreationForm()
    context["login_form"] = AuthenticationForm()
    return context


# === SECTION Home Page: auth only ===
class Home(TemplateView):
  template_name = "home.html"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # context["projects"] = Project.objects.all()
      return context


# === SECTION Login Page (might delete) ===
""" class Login(TemplateView):
  def get(self, request):
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "registration/login.html", context)

  def post(self, request):
    
      form = AuthenticationForm(request.POST)
      if form.is_valid():
          user = form.save()
          return redirect("home_redirect")
      else:
          context = {"form": form}
          return render(request, "registration/login.html", context)
    
@method_decorator(login_required, name='dispatch')
class HomeRedirect(View):
  def get(self, request):
    return redirect('/home/') """



# === SECTION Signup Page (might delete) ===
class Signup(TemplateView):

  def get(self, request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)

  def post(self, request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # Profile.objects.create(location=request.POST.get('location'), user=user)
      login(request, user)
      return redirect("profile_update")
    else:
      context = {"form": form}
      return render(request, "registration/signup.html", context)


# # === SECTION Profile Views ===

# Profile Create
class Create_Profile(CreateView): #CreateView
  model = Profile
  fields = ['id', 'location', 'image', 'user_id']
  template_name = "profile_create.html"
  success_url = "/profile/"

# Profile Read
class Profile(DetailView):
  model = Profile
  template_name = "profile.html"

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get("name")
    if name != None:
      context[""]

# Profile Update
class Update_Profile(TemplateView):
  template_name = "update_profile.html"
# class Update_Profile(ModelForm):


# @method_decorator(login_required, name='dispatch')
# class UserProfile(DetailView):
#   model= Profile
#   template_name="profile.html"

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context["projects"] = Project.objects.filter(user=self.object.pk)
#     form = Update_Profile(instance=self.object)
#     context["form"] = form
#     return context



# # === SECTION Project Views ===

# Project Create
class ProjectCreate(CreateView):
  model = Project
  fields = ['title', 'img', 'collaborators', 'location', 'about', 'skills_needed', 'skills_teachable', 'project_owner']
  template_name = "project_create.html"
  success_url = "/project/"

# Project Read

class Project(TemplateView):
  template_name = "project.html"
  
class ProjectList(TemplateView):
  template_name = "project_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["projects"] = Project.objects.all()
    return context

# # Project Update
# class Update_Project(TemplateView):
#   template_name = "update_project.html"

# # Project Delete
# # class Delete_Project()

# class SkillList(TemplateView):
#   template_name = "skill_list.html"

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context["skills"] = Skill.objects.all()
#     return context

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

