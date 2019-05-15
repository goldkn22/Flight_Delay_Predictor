from django import forms
from datetime import datetime, date

AIRLINE_CHOICES = (
    ('AA', 'American Airlines'),
    ('DL', 'Delta Airlines'),
    ('UA', 'United Airlines'),
    ('WN', 'Southwest Airlines'),
    ('B6', 'JetBlue Airlines'),
)


class InputForm(forms.Form):
    airline = forms.ChoiceField(choices=AIRLINE_CHOICES)
    flight_number = forms.CharField(label='Flight Number', max_length=10)
    date_year = forms.CharField(label='Year', max_length=4)
    date_month = forms.CharField(label='Month', max_length=2)
    date_day = forms.CharField(label='Day', max_length=2)
    #date = forms.DateField(widget=forms.SelectDateWidget(),initial=date.today())
