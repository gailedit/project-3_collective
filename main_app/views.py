from django.shortcuts import render, redirect
from django.urls import reverse

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
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
  template_name = "home.html"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # context["projects"] = Project.objects.all()
      return context


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
      return redirect("profile_create")
    else:
      context = {"form": form}
      return render(request, "registration/signup.html", context)


# # === SECTION Profile Views ===

# Profile Create
@method_decorator(login_required, name='dispatch')
class ProfileCreate(CreateView): #CreateView
  model = Profile
  fields = ['location', 'image', 'about', 'skills_current', 'skills_learn']
  template_name = "profile_create.html"
  success_url = "/profile/"

  def get_success_url(self): 
    return reverse('profile', kwargs={'pk': self.object.pk})

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(ProfileCreate, self).form_valid(form)


# Profile Read
@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
  model = Profile
  template_name = "profile_detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # context = ["projects"] = Project.objects.filter(title=self.object.pk)
    form = ProfileUpdateForm(instance=self.object)
    form = ProjectCreateForm()
    context["form"] = form
    return context

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'image', 'about', 'skills_current', 'skills_learn']

# Profile Update
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(View):

  def post(self, request, pk):
    form = ProfileUpdateForm(request.POST)
    if form.is_valid():
      Profile.objects.filter(user=pk).update(location=request.POST.get('location'), image=request.POST.get('image'), about=request.POST.get('about'), skills_current=request.POST.get('skills_current'), skills_learn=request.POST.get('skills_learn'))
      return redirect("profile", pk=pk)
    else:
      context = {"form": form, "pk": pk}
      return render(request, "profile_detail.html", context)

# Profile Delete
@method_decorator(login_required, name='dispatch')
class ProfileDelete(DeleteView):
    model = Profile
    template_name="profile_delete_confirmation.html"
    success_url="/"

@method_decorator(login_required, name='dispatch')
class ProfileRedirect(View):
  def get(self, request):
    return redirect('profile', request.user.profile.pk)

# # === SECTION Project Views ===

# Project Create

class ProjectCreateForm(ModelForm):
  class Meta:
    model = Project
    fields = ['title', 'img', 'collaborators', 'location', 'about', 'skills_needed', 'skills_teachable', 'project_owner']

class ProjectCreate(View):
  def post(self, request, pk):
    title = request.POST.get("title")
    location = request.POST.get("location")
    about = request.POST.get("about")
    collaborators = request.POST.get("collaborators")
    project_owner = request.POST.get("project_owner")
    skills_needed = request.POST.get("skills_needed")
    skills_teachable = request.POST.get("skills_teachable")

    Project.objects.create(title=title, location=location, about=about, collaborators=collaborators, project_owner=project_owner, skills_needed=skills_needed, skills_teachable=skills_teachable)
    return redirect()


# Project Read
class ProjectDetail(DetailView):
  model = Project
  template_name = "project_detail.html"
  
class ProjectList(TemplateView):
  template_name = "project_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["projects"] = Project.objects.all()
    return context

# # Project Update
# class ProjectUpdate(TemplateView):
#   template_name = "update_project.html"

# Project Delete
class ProjectDelete(DeleteView):
  model = Project
  template_name = "project_delete_confirmation.html"
  success_url = "profile"

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

