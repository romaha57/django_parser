from django import forms

from .models import User
from .user_info import DEFAULT_VAlUE_CITY, LIST_OF_CITIES, LIST_OF_LANGUAGE


class ProfileChangeForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'readonly': True}))
    city = forms.ChoiceField(choices=LIST_OF_CITIES, widget=forms.Select(attrs={
        'class': 'form-control'}))
    language = forms.ChoiceField(choices=LIST_OF_LANGUAGE, widget=forms.Select(attrs={
        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'city', 'language')