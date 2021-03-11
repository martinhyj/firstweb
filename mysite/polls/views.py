'''
Author: martin
Date: 2021-02-23 16:15:36
LastEditTime: 2021-03-10 21:13:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mysite/polls/views.py
'''

from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic

from django.utils import timezone
from .models import Question,Choice,Teacher
from rest_framework.response import Response
from .serializers import TeacherSerializers
import json

# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[0:5]
#     context={
#         'latest_questions': latest_question_list,
#     }
#     return render(request,'polls/index.html',context)

# def detail(request, question_id):

#     question=get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/detail.html',{'question':question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s"
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def results(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


'''
    Teacher
    add, delete, update, search
'''
from rest_framework.views import APIView

class TeacherAPIView(APIView):
    
    def get(self,request):
        page=int(self.request.query_params.get('page',0))
        num=int(self.request.query_params.get('num',0))
        end=page*num
        start=end-num
        teachers_serializer=TeacherSerializers(Teacher.objects.all()[start:end],many=True)
        result={"data":teachers_serializer.data}
        result["total"]=len(Teacher.objects.all())
        return HttpResponse(json.dumps(result),content_type='application/json')
        # json.dumps(teachers_serializer.data)

class TeacherCreate(APIView):

    def post(self, request):
        data=json.loads(request.body)
        T=Teacher(teacher_name=data["name"],teacher_age=int(data["age"]),teacher_major=data["major"],\
            teacher_department=data["department"],teacher_sex=data["sex"])
        T.save()
        return HttpResponse("200")
        
class TeacherDelete(APIView):

    def delete(self,request):
        id=int(request.query_params.get('id','-1'))
        if id>=0:
            T=Teacher.objects.filter(id=id).delete()
            return HttpResponse(status="200")
        else: return Http404


class TeacherUpdate(APIView):

    def post(self,request):

        # print(json.loads(request.body))
        data=json.loads(request.body)
        if data["id"]>0:
            Teacher.objects.filter(id=data["id"]).update(teacher_name=data["name"],\
                teacher_age=int(data["age"]),teacher_major=data["major"],\
                teacher_department=data["department"],teacher_sex=data["sex"])
            return HttpResponse("200")
        else:
            return HttpResponse("404")
