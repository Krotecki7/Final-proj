from django import forms
from django.forms import ModelForm

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = (
            "name",
            "text",
        )

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название записи"}
        )
        self.fields["text"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите текст"}
        )
