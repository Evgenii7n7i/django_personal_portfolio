from django.urls import path
from .import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('about/', views.about_the_project, name='about'),
]