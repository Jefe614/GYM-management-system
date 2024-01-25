from django.shortcuts import render
from .models import Image, Service, ServiceDetails
# Create your views here.

def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

    