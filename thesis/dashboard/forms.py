from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile


def file_size(value: InMemoryUploadedFile):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError("File too large. Size should not exceed 5 MiB.")


def file_extension(value: InMemoryUploadedFile):
    if not value.name.endswith(".csv"):
        raise ValidationError("Invalid file extension. Only .csv files are allowed.")


class CSVUploadForm(forms.Form):
    file = forms.FileField(
        allow_empty_file=False, validators=[file_size, file_extension]
    )
