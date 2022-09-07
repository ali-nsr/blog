from django.urls import path
from . import views

app_name = 'signalsafar'
urlpatterns = [
    path('', views.home, name='home')
]
