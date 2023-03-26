from django import forms
from .models import TodoModel, User, Profile
from django.contrib.auth.forms import UserCreationForm









class LoginForm(UserCreationForm):

    username = forms.CharField(min_length=5, max_length=30, label='Username', widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg shadow-sm bg-white rounded border-gold'}))
    password1 = forms.CharField(min_length=5, max_length=30, label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control form-control-lg shadow-sm bg-white rounded border-gold'}))
    
    
    class Meta:
        model = User
        fields = ['username','password1']




class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'memo', 'important']
        widgets = {
          'memo': forms.Textarea(attrs={'class' : 'form-control shadow-sm rounded article'}),
          'title': forms.TextInput(attrs={'class' : 'form-control shadow-sm rounded article'}),
          'important': forms.CheckboxInput(attrs={'class' : 'form-check-input checkboxes'}),
        }



class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(min_length=5, max_length=30, label='Username', widget=forms.TextInput(attrs={'class' : 'form-control shadow-sm bg-white rounded border-gold'}))
    password1 = forms.CharField(min_length=8, max_length=30, label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control shadow-sm bg-white rounded border-gold'}))
    password2 = forms.CharField(min_length=8, max_length=30, label='Password confirmation', widget=forms.PasswordInput(attrs={'class' : 'form-control shadow-sm bg-white rounded border-gold'}))
    email = forms.EmailField(max_length=50, label='Email', widget=forms.EmailInput(attrs={'class' : 'form-control shadow-sm bg-white rounded border-gold'}))
    
    class Meta:
        model = User
        fields = ['username','password1','password2','email']


class ResetForm(forms.ModelForm):

    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class' : 'form-control form-control-lg shadow-sm bg-white rounded border-gold'}))
    
    class Meta:
        model = User
        fields = ['email']  


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control shadow-sm rounded updatep'}))
    last_name = forms.CharField(min_length=2, max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control shadow-sm rounded updatep'}))
    email = forms.EmailField(min_length=2, max_length=50, widget=forms.EmailInput(attrs={'class' : 'form-control shadow-sm rounded updatep'}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UpdateProfilePicture(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']


