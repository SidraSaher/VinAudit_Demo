from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate


class FilterForm(forms.Form):

    year_make_model = forms.CharField(required = True,widget=forms.TextInput(attrs={'placeholder': 'Eg. 2015 Toyota Camry ','class': "col-md-6 form-control"}))
    mileage = forms.CharField(required = False,widget=forms.TextInput(attrs={'placeholder': 'Eg. 150,000 ','class': "col-md-6 form-control"}))
    
    class Meta:
        fields = ("year_make_model")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       