from django.shortcuts import render
from .models import *


def portfolio(request):
    title = 'Портфолио'
    project = Project.objects.all()
    context = {'title': title, 'project': project}
    return render(request, 'portfolio/portfolio.html', context)


def about_the_project(request):
    title = 'Проект Портфолио'
    text = 'My test text'
    context = {'title': title, 'text': text}
    return render(request, 'portfolio/about.html', context)
