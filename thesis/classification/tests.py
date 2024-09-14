from django.test import TestCase
from .models import ClassificationReport


class ClassificationReportTestCase(TestCase):
    def setUp(self):
        ClassificationReport.objects.create(
            predicted_text="This is a test",
            predicted_class="test",
            expected_class="test",
        )

    def test_classification_report_str(self):
        report = ClassificationReport.objects.get(predicted_text="This is a test")
        self.assertEqual(report.predicted_text, "This is a test")
        self.assertEqual(report.predicted_class, "test")
        self.assertEqual(report.expected_class, "test")
        self.assertEqual(str(report), "This is a test [test - test]")
