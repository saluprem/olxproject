from django import forms
from vehicle.models import vehicles
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    
class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=vehicles
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "owner":forms.TextInput(attrs={"class":"form-control"}),
            "mob":forms.NumberInput(attrs={"class":"form-control"})

        }