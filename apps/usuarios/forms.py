from typing import Any
from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(
        label ='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Joao Silva',
            }
        )
    )
    senha = forms.CharField(
        label ='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',

            }
        )
    )

class CadastroForm(forms.Form):
    nome = forms.CharField(
        label ='Nome de Cadastro',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Joao Silva',
            }
        )
    )
    email = forms.EmailField(
        label ='Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: JoaoSilva@gmail.com',
            }
        )
    )
    senha1 = forms.CharField(
        label ='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',

            }
        )
    )
    senha2 = forms.CharField(
        label ='Confirme a Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',

            }
        )
    )

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Nao pode ter espaços')
            
    def clean_senha2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')

        if senha1 and senha2:
            if senha2 != senha1:
                raise forms.ValidationError('Senhas diferentes')
            else:
                return senha2

