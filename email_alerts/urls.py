from django.urls import path, include
from . import views 

urlpatterns = [
    # path('index', views.index, name='index'),
    path('emails/', views.send_email_notification),
]