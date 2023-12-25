from django.urls import path,include
from rest_framework import routers
from . import views


app_name="api"

router = routers.DefaultRouter()
router.register('item',views.ItemViewSet)

urlpatterns = [
    # path('',include(router.urls)),
    path('data',views.DumpApiView.as_view()),
    path('home',views.home,name='home'),
    path('index',views.index,name='index'),
    path('post_data',views.post_data,name='post_data'),




   
]