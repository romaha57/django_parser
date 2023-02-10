from django import forms

from .models import City, Language
from app_users.models import User


class HomePageForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  empty_label='Выберите город', to_field_name='name',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    language = forms.ModelChoiceField(queryset=Language.objects.all(), to_field_name='name',
                                      empty_label='Выберите язык программирования',
                                      widget=forms.Select(attrs={'class': 'form-control'
    }))
