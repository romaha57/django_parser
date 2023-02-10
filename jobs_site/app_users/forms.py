from django import forms

from .models import User
from app_jobs.models import City, Language


class ProfileChangeForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'}), label='Имя пользователя')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'readonly': True}), label='Email')
    city = forms.ModelChoiceField(required=True,
                                  empty_label='Изменить город',
                                  queryset=City.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}), label='Город')
    language = forms.ModelChoiceField(required=True,
                                      empty_label='Изменить язык программирования',
                                      queryset=Language.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}), label='Язык программирования')

    class Meta:
        model = User
        fields = ('username', 'email', 'city', 'language')