from django import forms
from .models import UserImageDb


class UploadForm(forms.ModelForm):

    class Meta:
        model = UserImageDb
        fields = ['name', 'user_image']