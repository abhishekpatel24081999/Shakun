from django import forms
from .models import Conform

class ConformForm(forms.ModelForm):
    class Meta:
        model = Conform
        fields = '__all__'
        

