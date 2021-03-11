'''
Author: your name
Date: 2021-02-23 15:19:55
LastEditTime: 2021-03-07 21:00:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mysite/mysite/urls.py
'''
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from polls.views import TeacherAPIView,TeacherCreate,TeacherDelete,TeacherUpdate


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    url('api/list',TeacherAPIView.as_view()),
    url('api/create',TeacherCreate.as_view()),
    url('api/delete',TeacherDelete.as_view()),
    url('api/update',TeacherUpdate.as_view())
]
urlpatterns+=staticfiles_urlpatterns()