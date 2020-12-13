"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from webapp.views import musicians_list_view, index_view, musician_view, musician_get_view, \
    musician_add_view, musician_edit_view, musician_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('musicians', musicians_list_view, name='musicians_list'),
    path('musicians/get', musician_get_view, name='musician_get'),
    path('musicians/add', musician_add_view, name='musician_add'),
    path('musicians/<int:pk>', musician_view, name='musician'),
    path('musicians/<int:pk>/edit', musician_edit_view, name='musician_edit'),
    path('musicians/<int:pk>/delete', musician_delete_view, name='musician_delete'),
    path('admin/', admin.site.urls),
]

