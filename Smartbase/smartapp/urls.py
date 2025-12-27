from django.urls import path,include
from smartapp import views

urlpatterns = [
    path('',views.base,name='base'),
    path('apply/',views.submit_application,name='apply_form'),
    path('track/', views.track_status, name='track_status'),
    path('test/', views.test, name='test'),
    
]