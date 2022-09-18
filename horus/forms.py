from django import forms
from .models import sendEmail

class FormularioHorus(forms.ModelForm):
    class Meta:
        model = sendEmail
        fields = '__all__'

