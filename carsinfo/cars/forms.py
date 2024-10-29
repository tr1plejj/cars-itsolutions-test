from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from cars.models import Car, Comment


User = get_user_model()


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (
            'make',
            'model',
            'year',
            'description',
        )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'content',
        )