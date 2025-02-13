from datetime import datetime
from django import forms

class CreateEventForm(forms.Form):

    def __init__(self, *args, categories, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categories"].choices = [(cat.id, cat.name) for cat in categories]

    title = forms.CharField(required=True, label="Nome do evento")
    address = forms.CharField(label="Endereco")
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type':'date',
            'max': datetime.now().date()
        }),
        label="Data do evento"
    )
    quantity = forms.IntegerField(label="Quantidade de Ingressos")
    categories = forms.ChoiceField(choices=[], label="Escolha uma categoria")
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        label="Descricao do evento"
    )


