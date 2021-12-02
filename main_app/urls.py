from django.urls import path
from . import views

urlpatterns = [
  path('', views.Landing.as_view(), name="landing"),
  path('home/', views.Home.as_view(), name="home"),

  # path('accounts/login/', views.Login.as_view(), name="login"),
  path('accounts/signup/', views.Signup.as_view(), name="signup"),

  path('profile/<int:pk>', views.Profile.as_view(), name="profile"),
  path('profile/update/', views.Update_Profile.as_view(), name="profile_update"),
  path('profile/create/', views.Create_Profile.as_view(), name="profile_create"),

  path('project/new/', views.ProjectCreate.as_view(), name="project_create"),
  path('project/', views.Project.as_view(), name="project"),
  # path('project/update/', views.Update_Project.as_view(), name="project_update"),
  # path('projects/', views.ProjectList.as_view(), name="project_list"),

  path('about/', views.About.as_view(), name="about"),
  path('about-dev/', views.About_Dev.as_view(), name="about_dev"),
]