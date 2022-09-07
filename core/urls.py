"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('home.urls')),
    path('', include('django.contrib.auth.urls')),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('', include('blog.urls')),
    path('account/', include('accounts.urls')),
    path('comment/', include('comment.urls')),
    path('', include('contact_us.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('admin.signalsafar/', admin.site.urls),
]

handler404 = 'home.views.handle_404_error'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                      document_root=settings.STATIC_ROOT)
