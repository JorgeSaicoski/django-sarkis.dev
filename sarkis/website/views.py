from django.shortcuts import render
from skills.models import Category, Service, Skill
from projects.models import Project
from website.forms import ContactForm
import random


# Create your views here.

def home(req):
    categories = Category.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()

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
    skills = Skill.objects.all()

    context = {
        'skills': skills,
    }
    return render(req, 'website/skills_page.html', context)

first = int(random.randint(0,9))
second = int(random.randint(0,9))


def contact(request):

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        restart()
        if form.is_valid():
            form.save()
            return render(request, "website/contact_thanks.html", {"name": request.POST["name"]})
        else:
            print("PROBLEM")

    context = {"form": form,"first": first,"second": second}
    return render(request, "website/contact.html", context)
