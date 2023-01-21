from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Comment, Rating
from django import forms


class LoginForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'quantity', 'email', 'phone', 'city', 'street', 'house', 'good', 'user']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['good', 'date', 'text']

    # def widgets(self):

class RateForm(ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'


# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'phone', 'email', 'message']
