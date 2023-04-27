from django import forms
from .models import imgForm

class imgFormWithModel(forms.ModelForm):
    class Meta:
        model = imgForm
        fields = "__all__"
