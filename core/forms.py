from django import forms
from django.forms import ModelForm
from .models import Data, Play

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
    plays_seen = forms.ModelMultipleChoiceField(
        queryset=Play.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )