from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import Userprofile

class signUpForm(UserCreationForm):
    Email= forms.EmailField(required=True,label="Email Address")
    
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')
 


class Userprofilechange(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')
        
        

class profile_picture(forms.ModelForm):
    class Meta:
        model= Userprofile
        fields=['profile_picture']        