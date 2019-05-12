from django import forms
from datetime import datetime



AIRLINE_CHOICES = (
    ('AA', 'American Airlines'),
    ('DAL', 'Delta Airlines'),
    ('UAL', 'United Airlines'),
)


class InputForm(forms.Form):
    airline = forms.ChoiceField(choices=AIRLINE_CHOICES)
    flight_number = forms.CharField(label='Flight Number', max_length=10)
    date = forms.DateField(widget=forms.SelectDateWidget)
    #date = forms.DateTimeField(datetime.now())
