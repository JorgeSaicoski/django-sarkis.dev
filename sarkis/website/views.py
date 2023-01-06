from django.shortcuts import render
from skills.models import Category, Service
from projects.models import Project


# Create your views here.

def home(req):
    categories = Category.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()


    context = {
        'categories': categories,
        'services': services,
        'projects': projects
    }
    return render(req, 'website/home.html', context)
