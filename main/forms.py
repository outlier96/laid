from django import  forms
from django.forms import ModelForm
from .models import User,Login

# create a user form
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('fname','lname', 'email','password','tel')
        labels ={ 
            'fname':'enter your first Name',
            'lname': 'enter your Lat Name', 
            'email': 'enter your email address',
            'password':'enter your password',
            'tel': 'enter phone number',}
        widget = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your first'}),
            'lname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your lastname'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email address'}),
            'password': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your password'}),
            'tel': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your password'}),

        }


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"