from django.urls import path ,include
from . import views

app_name='web'

urlpatterns = [

    path('',views.index , name='index'),
    path('api/v1/normalize/',views.normalize , name='index'),
]