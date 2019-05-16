from django import forms
from datetime import datetime, date

AIRLINE_CHOICES = (
    ('AA', 'American Airlines'),
    ('DL', 'Delta Airlines'),
    ('UA', 'United Airlines'),
    ('WN', 'Southwest Airlines'),
    ('B6', 'JetBlue Airlines'),
)

#Input form widgets
class InputForm(forms.Form):
    airline = forms.ChoiceField(label='airline', choices=AIRLINE_CHOICES,widget=forms.Select(attrs={'class': 'form-control'}))
    flight_number = forms.CharField(label='flight_number', max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_year = forms.CharField(label='Year', max_length=4,widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_month = forms.CharField(label='Month', max_length=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_day = forms.CharField(label='Day', max_length=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
