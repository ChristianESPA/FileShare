from django import forms
from .models import UploadFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(),
            'file': forms.ClearableFileInput(),
        }
