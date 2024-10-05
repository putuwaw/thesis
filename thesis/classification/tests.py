from django.test import TestCase, Client
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


class ClassificationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
