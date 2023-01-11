from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('project/<str:pk>', views.project, name="project"),
	path('projects', views.projects, name="projects"),
	path('skills', views.skills, name="skills"),

]