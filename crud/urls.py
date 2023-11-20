"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from registro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('add/', views.add, name='add'),
    path('add_person/', views.add_person, name='add_person'),
    path('delete_selected_users/', views.delete_selected_users, name='delete_selected_users'),
    path('delete_person/', views.delete_person, name='delete_person'),
    path('edit_person/', views.edit_person, name='edit_person'),
    path('test_add_person/', views.test_add_person, name='test_add_person'),
    path('get_all_persons/', views.get_all_persons, name='get_all_persons'),
]
