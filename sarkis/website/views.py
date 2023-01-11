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

def project(req, pk):
    project = Project.objects.get(name=pk)
    sub_services = project.get_sub_services
    skills = project.get_skills

    context = {
        'sub_services': sub_services,
        'project': project,
        'skills': skills
    }
    return render(req, 'website/project.html', context)
def projects(req):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return render(req, 'website/projects_page.html', context)

def skills(req):
    skills =  Skill.objects.all()

    context = {
        'skills': skills,
    }
    return render(req, 'website/skills_page.html', context)

