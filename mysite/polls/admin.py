'''
Author: your name
Date: 2021-02-23 16:15:36
LastEditTime: 2021-03-08 20:14:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mysite/polls/admin.py
'''

# Register your models here.
from django.contrib import admin

from .models import Question, Choice,Teacher

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    # fields=['pub_date', 'question_text']

    fieldsets=[
        (None,              {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'], 'classes':
        ['collapse']})
    ]
    
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']

class TeacherAdmin(admin.ModelAdmin):
    search_fields=['teacher_name']
    list_display=('id','teacher_name','teacher_age','teacher_sex','teacher_department')

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Teacher,TeacherAdmin)