from . models import Todo
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        permission = [IsAuthenticated]
        fields   = ['task','timestamp','completed','updated','user']
