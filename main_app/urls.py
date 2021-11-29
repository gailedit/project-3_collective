from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('login', views.Login.as_view(), name="login"),
  path('signup', views.Signup.as_view(), name="signup"),
  path('profile/', views.Profile.as_view(), name="profile"),
  path('update-profile/', views.Update_Profile.as_view(), name="update-profile"),
  path('project/', views.Project.as_view(), name="project"),
  path('about/', views.About.as_view(), name="about"),
  path('about-dev/', views.About_Dev.as_view(), name="about-dev"),
  # path('skills/', views.SkillList.as_view(), name="skills_list"),
]