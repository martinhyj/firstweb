'''
Author: martin
Date: 2021-02-23 16:16:53
LastEditTime: 2021-03-07 17:02:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mysite/polls/urls.py
'''
from django.urls import path

from . import views

app_name="polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]