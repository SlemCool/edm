from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Document


class DocumentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["doc_type"].empty_label = "Выберите тип документа"

    class Meta:
        model = Document
        fields = [
            "doc_type",
            "from_doc",
            "where_doc",
            "area",
            "who",
            "theme",
            "detail",
            "given",
            "file",
            "description",
            "implementers",
            "date_input_doc",
            "date_output_doc",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "date_input_doc": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"type": "date"}
            ),
            "date_output_doc": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"type": "date"}
            ),
        }

    def clean_text(self):
        description = self.cleaned_data["description"]
        if "Трамп" in description:
            raise ValidationError("Не допустимо упоминание Трампа в Документе!")
        return description


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']
