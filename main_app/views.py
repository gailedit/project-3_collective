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

class Landing(TemplateView):
  template_name = "landing.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["signup_form"] = UserCreationForm()
    context["login_form"] = AuthenticationForm()
    return context

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

class Project:
  def __init__(self, title, image, location, about):
    self.title = title
    self.image = image
    self.location = location
    self.about = about

projects = [
  Project("Super Cool Art Project", "https://www.google.com/url?sa=i&url=https%3A%2F%2Fu.osu.edu%2Fhill.1523%2F2015%2F10%2F19%2Fexhibition-proposal-draft%2F&psig=AOvVaw2GCcCAueSo7Fukd4vfJiB8&ust=1638402389939000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKi7iNeiwfQCFQAAAAAdAAAAABAD", "Petaluma", "My piece takes the shape of a tree using panels of wood arranged in a semi-circular setup around a tree stump. There will be an opening in which the viewer can sit on the stump inside of the panels. I would like my piece to be placed in a corner in which the viewer can walk around the piece as well as sit inside of it. The piece is made up almost entirely of wood and will have a sound element. The stump will be elevated using pieces of wood and the sound will be placed beneath the stump. I would like to run the wires from the speaker up one of the back planks into the ceiling. I will provide the speaker but will need someway to play the sound. The piece is about 8 feet tall and 4 feet in all directions. I will also need to use your track lighting system."),
  Project("Untitled", "https://cdna.artstation.com/p/assets/images/images/018/966/814/large/maria-benita-a-img-20161027-wa0005.jpg?1561450038", "Reno, NV", "It's a time travel machine. I know it sounds crazy, but I've gotten it to work once before - I just need someone who knows arduino to really make this a viable product"),
]

class ProjectList(TemplateView):
  template_name = "project_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["projects"] = projects

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

