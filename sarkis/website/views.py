from django.shortcuts import render
from skills.models import Category, Service


# Create your views here.

def home(req):
    categories = Category.objects.all()
    services = Service.objects.all()


    context = {
        'categories': categories,
        'services': services
    }
    return render(req, 'website/home.html', context)
