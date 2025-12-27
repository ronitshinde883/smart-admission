from django.urls import path,include
from smartapp import views

urlpatterns = [
    path('',views.home,name='home page')
]