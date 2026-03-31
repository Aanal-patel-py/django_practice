from django import forms

class Registration(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()


