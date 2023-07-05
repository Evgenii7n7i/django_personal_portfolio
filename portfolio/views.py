from django.shortcuts import render
from .models import *


def portfolio(request):
    title = 'Портфолио'
    project = Project.objects.order_by('title')
    context = {'title': title, 'project': project}
    return render(request, 'portfolio/portfolio.html', context)
