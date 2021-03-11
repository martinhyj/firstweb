'''
Author: martin
Date: 2021-02-23 16:15:36
LastEditTime: 2021-03-08 18:44:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mysite/polls/models.py
'''

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Teacher(models.Model):

    def __str__(self):
        return self.teacher_name    
    
    class Meta:
        pass
        
    APIKEY=models.CharField(max_length=30,verbose_name='APIkey',default='abcdefghijklmn')
    # property
    teacher_name=models.CharField(max_length=10)
    teacher_age=models.IntegerField(default=0)
    teacher_department=models.CharField(max_length=20)
    teacher_major=models.CharField(max_length=20)
    teacher_sex=models.CharField(max_length=10,default="")
    

class Question(models.Model):
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<=now

        
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Published recently?'


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)