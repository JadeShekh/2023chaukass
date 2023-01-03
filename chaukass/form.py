from unittest.util import _MAX_LENGTH
from django import forms
 
# creating a form
class InputForm(forms.Form):
 
    imei = forms.CharField(max_length = 25)
    msg = forms.CharField(max_length = 50)
    lat = forms.FloatField(
                     help_text = "Enter 6 digit roll number"
                     )
    long = forms.FloatField(
                     help_text = "Enter 6 digit roll number"
                     )
    samay=forms.FloatField(max_value=1000)