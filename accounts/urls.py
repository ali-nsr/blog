from django.urls import path
from .views import Profile, ProfileImage


app_name = 'account'
urlpatterns = [
    # path('', ArticleList.as_view(), name='home'),
    path('profile', Profile.as_view(), name='profile'),
    path('profile-image', ProfileImage.as_view(), name='profile_image'),
]
