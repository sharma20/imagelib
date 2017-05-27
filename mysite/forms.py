from django import forms
from .models import UserImage, User

# Image upload form variables


class ImageUploadForm(forms.ModelForm):
    image = forms.ImageField()
    caption = forms.CharField()

    class Meta:
        model = UserImage
        fields = ('image', 'caption')


# User Registration form variables

class RegisterForm(forms.ModelForm):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField()

    class Meta:
        model = User
        fields = ('name', 'password', 'email')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())