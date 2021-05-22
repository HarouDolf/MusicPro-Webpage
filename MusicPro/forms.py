from django import forms

class AñadirAlCarroForm(forms.Form):
    cantidad = forms.IntegerField()