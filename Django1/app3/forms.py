from django import forms

class Registration(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    gender_choices=[
        ('male','Male'),
        ('female','Female'),
    ]
    gender=forms.ChoiceField(choices=gender_choices,label="select gender")



