from django.shortcuts import render, get_object_or_404
from .models import *

def all_blogs(request):
    title = 'Мои блоги'
    # Включение сортировки по дате
    blogs = Blog.objects.order_by('-date')
    context = {'title': title, 'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context)


def detail(request, blog_id):
    '''
    функция припомощи get_object_or_404 либо откроет нужную 
    страницу, либо покажет ошибку 404

    '''
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})