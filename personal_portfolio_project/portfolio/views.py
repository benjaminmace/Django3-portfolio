from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request=request, template_name='portfolio/home.html', context={'projects':projects})


