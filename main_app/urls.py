from django.urls import path
from . import views

urlpatterns = [
  path('', views.Landing.as_view(), name="landing"),
  path('home/', views.Home.as_view(), name="home"),

  path('accounts/signup/', views.Signup.as_view(), name="signup"),

  path('profile/<int:pk>/', views.ProfileDetail.as_view(), name="profile"),
  path('profile_redirect/', views.ProfileRedirect.as_view(), name="profile_redirect"),
  path('profile/create/', views.ProfileCreate.as_view(), name="profile_create"),
  path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
  path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name="profile_delete"),

  path('profile/<int:pk>/projects/new/', views.ProjectCreate.as_view(), name="project_create"),
  path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project"),
  # path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name="project_update"),
  path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name="project_delete"),
  # path('projects/', views.ProjectList.as_view(), name="project_list"),

  path('about/', views.About.as_view(), name="about"),
  path('about-dev/', views.About_Dev.as_view(), name="about_dev"),
]