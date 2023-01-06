from django.shortcuts import render
from skills.models import Category, Service, Skill
from projects.models import Project


# Create your views here.

def home(req):
    categories = Category.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    skills =  Skill.objects.all()


    context = {
        'categories': categories,
        'services': services,
        'projects': projects,
        'skills': skills
    }
    return render(req, 'website/home.html', context)
