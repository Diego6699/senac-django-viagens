from turtle import width
from django import forms
from django import forms
from tempus_dominus.widgets import DatePicker

class ViagemForms(forms.Form):
    origim = forms.CharField(label = 'Origem',max_length = 100)
    destino = forms.CharField(label= 'Destino',max_length= 100)
    data_ida = forms.DateField(label='Ida',widget = DatePicker())
    data_volta = forms.DateField(label='Volta',widget=DatePicker())
