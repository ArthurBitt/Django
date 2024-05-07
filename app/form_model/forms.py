from django import forms
from tempus_dominus.widgets import DatePicker

from .models import Passagem
from .validation import *

from .tipos_classe_voo import *
from app.form_model.models import Passagem,ClasseViagem,Pessoa


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class PassagemForms(forms.ModelForm):
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de Ida',
            'data_volta': 'Data de Volta',
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta':DatePicker()
        }

# class PassagemForms(forms.Form):
#     origem = forms.CharField(label='Origem', max_length=100)
#     destino = forms.CharField(label='Destino', max_length=100)
#     data_ida = forms.DateField(label='Ida', widget=DatePicker())
#     data_volta = forms.DateField(label='Volta', widget=DatePicker())
#     tipo_classes_voo = forms.ChoiceField(label='Classe', choices=tipo_classe_voo)


    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        lista_de_erros = {}
        is_a_number(origem, 'origem', lista_de_erros)
        is_a_number(destino, 'destino', lista_de_erros)
        origin_same_as_destiny(origem, destino, lista_de_erros)
        date_validation(data_ida, data_volta, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data