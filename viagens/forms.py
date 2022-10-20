from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from viagens.classe_viagem import tipos_de_classe

class ViagemForms(forms.Form):
    origim = forms.CharField(label = 'Origem',max_length = 100)
    destino = forms.CharField(label= 'Destino',max_length= 100)
    data_ida = forms.DateField(label='Ida',widget = DatePicker())
    data_volta = forms.DateField(label='Volta',widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa',disabled=True,initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Opção de voo',choices=tipos_de_classe)
    adicionais = forms.CharField(label= 'Informações adicionais',max_length=200,widget=forms.Textarea(),required=False)
    email = forms.EmailField(label='e-mail',max_length=200)
