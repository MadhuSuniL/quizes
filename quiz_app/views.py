from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import QuizSerializer
from .models import Quiz
from rest_framework.response import Response
from datetime import datetime , timedelta
from django.utils import timezone


class QuizGetAllView(GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    
    def get(self,request):
        quizzes = self.queryset.all()
        
        for quiz in quizzes:
            quiz.update_status()
        
        data = self.serializer_class(quizzes,many=True).data

        return Response(data)
    
class QuizRetrieveView(GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    
    def get(self,request,pk=None):
        if pk is not None:
            quiz = self.queryset.get(id=pk)
            quiz.update_status()            
            data = self.serializer_class(quiz).data
            return Response(data)
        return Response('Please provide pk(id) as endpoint in url!')

class QuizStatusWiseView(GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    
    def get(self,request,status):
        quizzes= self.queryset.filter(status=status.title())
        for quiz in quizzes:        
            quiz.update_status() 
                       
        data = self.serializer_class(quizzes,many=True).data
        return Response(data)
        

class QuizAnswerView(GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    
    def get(self,request,pk=None):
        if pk is not None:
            quiz = self.queryset.get(id=pk)
            quiz.update_status()            

            end_datetime_plus_5 = timezone.make_aware(datetime.combine(quiz.ends_date, quiz.ends_time)) + timedelta(minutes=5)
            current_datetime = timezone.now()
            
            if current_datetime > end_datetime_plus_5:
                return Response({'answer': quiz.answer})
            else:
                return Response({'message': 'The quiz answer will be available after 5 minutes of the end time.'})
            
            
        

class QuizCreateView(GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    
    def post(self,request):
        question = request.data['question']
        options = request.data['options']
        answer = request.data['answer']
        start_time = request.data['start_time'] #2023 12 03 01 05
        end_time = request.data['end_time']
        
        values_for_start = start_time.split()
        start_datetime = datetime(year=int(values_for_start[0]),month=int(values_for_start[1]),day=int(values_for_start[2]), hour=int(values_for_start[3]), minute=int(values_for_start[4]))
        values_for_end = end_time.split()
        end_datetime = datetime(year=int(values_for_end[0]),month=int(values_for_end[1]),day=int(values_for_end[2]), hour=int(values_for_end[3]), minute=int(values_for_end[4]))
    
        
        quiz = Quiz.objects.create(quesion=question,
                                   options=options,
                                   answer=answer,
                                   starts_date=start_datetime.date(),
                                   starts_time=start_datetime.time(),
                                   ends_date=end_datetime.date(),
                                   ends_time=end_datetime.time()
                                   )        
        
        quiz.update_status()
        data = self.serializer_class(quiz).data    
        return Response(data)