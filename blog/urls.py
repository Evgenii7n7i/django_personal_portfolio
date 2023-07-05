from django.urls import path
from .import views


# для работы динамической ссылки в all_blogs.html
app_name = 'blog'


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
