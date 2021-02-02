from django import forms
from .models import Photo, PhotoGroup

class UploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'name',
            'caption',
            'photo',
            'photo_group',
        ]
        widgets = {
          'caption': forms.Textarea(attrs={'rows':5, 'cols':27}),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = PhotoGroup
        fields = [
            'name',
        ]