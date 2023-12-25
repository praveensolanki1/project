from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions




class TodoListApiView(APIView):
    permission_classes   = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        todos = Todo.objects.filter(user = request.user.id)
        serializer_data = TodoSerializer(todos,many = True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        data = {
            'task' :request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
            }

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
