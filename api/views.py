from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from rest_framework.views import APIView
from django.http import HttpResponse
from . serializers import ItemSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
from django.db.models.signals import post_save
from django.dispatch import receiver
from . forms import *
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.core.cache import cache

# Create your views here.
# @api_view(['GET'])
def home(request):
    item_obj = Item.objects.all()
    serializer_data = ItemSerializer(item_obj,many=True)
    data = cache.get("mykey")
    if data is None:
       data = 'inter'
       cache.set("mykey",data,60*15)

       
    return render(request,'api/index.html')

    # return Response({'status':200,'payload':serializer_data.data})
@api_view(['POST'])
def post_data(request):
    try:
       data = request.data
       serializer = ItemSerializer(data=request.data)
       if not serializer.is_valid():
           return Response({'status':status.HTTP_400_BAD_REQUEST,'mesasge':'some thing went wrong'})
       serializer.save()
       print(serializer)
       return Response({'status':200,'message':'its wokring'})
       
    except:
        return Response({'status':500,'payload':'not working'})
def index(request):
    item=Item.objects.all()
    if request.method=="POST":
       email = request.POST.get('email')
       Auth.objects.bulk_create()
       Auth.save()
       item=Item.objects.all()
       print('email is',email)
       return HttpResponse('its working')
    return render(request,'api/index.html',{'form':item})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = []

class DumpApiView(APIView):

    def get(self,request):
        data = Item.objects.all()
        new_data = ItemSerializer(data,many=True)
       
        return Response({'status':status.HTTP_200_OK,'payload':new_data.data})
        # else:
        #     return Response({'status':500,'messages':'invalid data'})
    
    def post(self,request):
       try:
           data = request.data
           serializer = ItemSerializer(data=request.data)
           if not serializer.is_valid():
              return Response({'status':status.HTTP_400_BAD_REQUEST,'mesasge':'some thing went wrong'})
           serializer.save()
           print(serializer)
           return Response({'status':200,'message':'its wokring'})
       
       except:
           return Response({'status':500,'payload':'not Working'})


    def put(self,request,id):
        instance = self.get_object(id=self.id)
        

    def patch(self,request):
        item_obj = Item.objects.get(id=request.data['id'])
        item_serializer = ItemSerializer(item_obj,data=request.data,partial=True)
        if not item_serializer.is_valid():
            print(item_serializer.errors)
            return Response({'status':403,'errors':item_serializer.errors,'message':"its' error"})
        item_serializer.save()
        return Response({'status':200,'messages':'your data has been successfully saved'})

      
    def delete(self,request):
        id = request.GET.get('id')
        data = Item.objects.get(id=id)
        data.delete()
        return Response({'status':200,'messages':'item successfully deleted'})
       
# @receiver(post_save,sender=User)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=UserProfile)
# def send_notification_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'New Record Added'
#         message = 'A new record has been added to MyModel.'
#         from_email = '[email protected]'
#         recipient_list = ['[email protected]']
#         send_mail(subject, message, from_email, recipient_list)        
    

# def get_name(request):

#     if request.method=='POST':
#         form = Newform(request.post)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('success')
#         else:
#             form = Newform()
#             return 
