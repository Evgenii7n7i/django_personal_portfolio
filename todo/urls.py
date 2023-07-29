from django.urls import path
from .import views


urlpatterns = [
    # Auth
    # Страница регистрации
    path('signup/', views.signupuser, name='signupuser'),
    # Страница выхода пользователя
    path('logout/', views.logoutuser, name='logoutuser'),
    # Страница входа пользователя
    path('login/', views.loginuser, name='loginuser'),


    # Todo
    # Домашняя страница
    path('', views.home , name='home'),
    # Страница создания задания
    path('create/', views.createtodo, name='createtodo'),
    # Страница просмотра заданий пользователя
    path('current/', views.currenttodos, name='currenttodos'),
    # Страница просмотра завершённых задач
    path('completed/', views.completedtodos, name='completedtodos'),
    # Страница просмотра и изменения заданий пользователя
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    # Путь(не страница, просто ссылка на функцию), для завершения задания пользователя
    path('todo/<int:todo_pk>/complete>', views.completetodo, name='completetodo'),
    # Путь (не страница, просто ссылка на функцию), для удаления записи пользователя
    path('todo/<int:todo_pk>/delete>', views.deletetodo, name='deletetodo'),
]