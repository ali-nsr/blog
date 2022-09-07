from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
