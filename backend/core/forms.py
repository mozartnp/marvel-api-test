from django import forms

class PesquisaPersonagens(forms.Form):
    nome = forms.CharField(
        widget=forms.CharField(
            attrs={'placeholder' : "Digite o nome certo do personagem, ou parcial"}
        )
    )
    nome_preciso = forms.BooleanField(default=False)
    password = forms.CharField(
        label= "Senha",
        widget=forms.PasswordInput(
            attrs={'placeholder' : "Digite sua senha"}
        )
    )