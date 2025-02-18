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
            'type':'date'
        }),
        label="Data do evento"
    )

    date_release_tickets = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date'
        }),
        label="Data de compra dos Ingressos",
        required=False 
    )

    quantity = forms.IntegerField(label="Quantidade de Ingressos")
    categories = forms.ChoiceField(choices=[], label="Escolha uma categoria")
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        label="Descricao do evento"
    )


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


