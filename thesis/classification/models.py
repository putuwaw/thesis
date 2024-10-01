from django.db import models
from django.utils import timezone


class ClassificationReport(models.Model):
    predicted_text = models.TextField()
    predicted_class = models.CharField(max_length=30)
    expected_class = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.predicted_text[:50]} [{self.predicted_class} - {self.expected_class}]"


class Dataset(models.Model):
    text = models.TextField()
    source = models.TextField(null=True, blank=True)
    label = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.text[:50]} [{self.label} - {self.category}]"
