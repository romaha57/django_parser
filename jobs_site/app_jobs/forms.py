from django import forms

from .models import City, Language


class HomePageForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  empty_label='Выберите город',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    language = forms.ModelChoiceField(queryset=Language.objects.all(),
                                      empty_label='Выберите язык программирования',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
