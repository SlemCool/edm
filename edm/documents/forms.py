from django import forms
from django.core.exceptions import ValidationError

from .models import Document


class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doc_type'].empty_label = 'Выберите тип документа'

    class Meta:
        model = Document
        fields = ['doc_type', 'from_doc', 'description']

    def clean_text(self):
        description = self.cleaned_data['description']
        if 'Трамп' in description:
            raise ValidationError('Не допустимо упоминание Трампа в Документе!')
        return description


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']