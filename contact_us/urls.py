from django.urls import path
from . import views

app_name = 'contact_us'
urlpatterns = [
    path('contact-us', views.contact_us, name='contact_us'),
    path('about-us', views.about_us, name='about_us'),
]
