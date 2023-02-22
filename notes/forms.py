from django import forms
from .models import NoteModel, CategoryModel
import re
from django.core.exceptions import ValidationError


class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['note_title', 'note_content', 'is_published', 'note_photo', 'category']
        widgets = {
            'note_title': forms.TextInput(attrs={'class': 'form-control'}),
            'note_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'category': forms.Select(attrs={'class': 'form-content'})
        }

    def clean_note_title(self):
        note_title = self.cleaned_data['note_title']
        if re.match(r'\d', note_title):
            raise ValidationError('Заголовок не должен начинаться с цифры')
        return note_title

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['title', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }