from django import forms

class LoginForm(forms.Form):
    username= forms.CharField(max_length=100)
    password= forms.CharField(max_length=100)
    ip= forms.CharField(max_length=100)
    port= forms.CharField(max_length=100)