'''
Author: your name
Date: 2021-03-07 17:41:34
LastEditTime: 2021-03-10 11:42:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mysite/polls/serializers.py
'''

from rest_framework import  serializers
from .models import Teacher

class TeacherSerializers(serializers.Serializer):
    id=serializers.IntegerField()
    teacher_age=serializers.IntegerField(default=0)
    teacher_name=serializers.CharField(required=True,max_length=100)
    teacher_department=serializers.CharField(required=True,max_length=100)
    teacher_major=serializers.CharField(required=True,max_length=100)
    teacher_sex=serializers.CharField(required=True,max_length=10)
