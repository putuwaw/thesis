from django.db import models
from django.utils import timezone


class ClassificationReport(models.Model):
    predicted_text = models.TextField()
    predicted_class = models.CharField(max_length=30)
    expected_class = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.predicted_text[:50]} [{self.predicted_class} - {self.expected_class}]"
