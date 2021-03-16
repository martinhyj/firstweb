'''
Author: your name
Date: 2021-03-07 17:41:34
LastEditTime: 2021-03-16 20:13:05
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
    teacher_sex=serializers.CharField(required=True, max_length=2)
    teacher_college=serializers.CharField(max_length=20,required=True)
    teacher_address=serializers.CharField(max_length=50,required=True)
    teacher_phone=serializers.CharField(max_length=11,required=True)
    teacher_salary=serializers.CharField(max_length=10,required=True)
    teacher_degree=serializers.CharField(max_length=20,required=True)
    teacher_hobby=serializers.CharField(max_length=20,required=True)
    teacher_height=serializers.CharField(max_length=10,required=True)
    teacher_weight=serializers.CharField(max_length=10,required=True)
    teacher_ismarry=serializers.CharField(max_length=10,required=True)
