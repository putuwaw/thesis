from django.test import TestCase, Client
from .models import ClassificationReport
from .thesis_ml.notebook import (
    MultinomialNB,
    TFIDF,
    LabelBinarizer,
    SMOTE,
    chi_square,
    split_data,
    accuracy_score,
)

import numpy as np


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


class TFIDFTestCase(TestCase):
    def setUp(self):
        self.tfidf = TFIDF()

    def test_tfidf_fit_transform(self):
        corpus = [
            "this is the first document",
            "this document is the second document",
            "and this is the third one",
            "is this the first document",
        ]

        X_tfidf = self.tfidf.fit_transform(corpus)
        self.assertTrue(
            np.array_equal(
                X_tfidf,
                np.array(
                    [
                        [
                            0.0,
                            0.46979138557992045,
                            0.5802858236844359,
                            0.38408524091481483,
                            0.0,
                            0.0,
                            0.38408524091481483,
                            0.0,
                            0.38408524091481483,
                        ],
                        [
                            0.0,
                            0.6876235979836938,
                            0.0,
                            0.281088674033753,
                            0.0,
                            0.5386476208856763,
                            0.281088674033753,
                            0.0,
                            0.281088674033753,
                        ],
                        [
                            0.511848512707169,
                            0.0,
                            0.0,
                            0.267103787642168,
                            0.511848512707169,
                            0.0,
                            0.267103787642168,
                            0.511848512707169,
                            0.267103787642168,
                        ],
                        [
                            0.0,
                            0.46979138557992045,
                            0.5802858236844359,
                            0.38408524091481483,
                            0.0,
                            0.0,
                            0.38408524091481483,
                            0.0,
                            0.38408524091481483,
                        ],
                    ]
                ),
            )
        )


class MultinomialNBTestCase(TestCase):
    def setUp(self):
        self.clf = MultinomialNB()

    def test_mnb_fit_predict(self):
        rng = np.random.RandomState(1)
        X = rng.randint(5, size=(6, 100))
        y = np.array([1, 2, 3, 4, 5, 6])

        self.clf.fit(X, y)
        prediction = self.clf.predict(X[2:3])

        self.assertEqual(prediction, [3])
        self.assertTrue(
            np.allclose(
                np.array(self.clf.join_log_likelihoods),
                np.array(
                    [
                        [
                            -980.3129721979368,
                            -981.8851425503753,
                            -911.9941418835292,
                            -988.5867956213812,
                            -997.0241252139006,
                            -995.704145875506,
                        ]
                    ]
                ),
            )
        )


class LabelBinarizerTestCase(TestCase):
    def setUp(self):
        self.label_binarizer = LabelBinarizer()

    def test_label_binarizer_fit_transform(self):
        y = [1, 2, 6, 4, 2]
        self.label_binarizer.fit(y)
        y_transformed = self.label_binarizer.transform([1, 6])
        self.assertTrue(
            np.array_equal(
                y_transformed,
                np.array([[1, 0, 0, 0], [0, 0, 0, 1]]),
            )
        )

        y = ["yes", "no", "no", "yes"]
        y_transformed = self.label_binarizer.fit_transform(y)
        self.assertTrue(
            np.array_equal(
                y_transformed,
                np.array([[1], [0], [0], [1]]),
            )
        )


class ChiSquareTestCase(TestCase):
    def test_chi_square(self):
        X = np.array([[1, 1, 3], [0, 1, 5], [5, 4, 1], [6, 6, 2], [1, 4, 0], [0, 0, 0]])
        y = np.array([1, 1, 0, 0, 2, 2])
        self.assertTrue(
            np.allclose(chi_square(X, y), np.array([15.38461538, 6.5, 8.90909091]))
        )


class SMOTETestCase(TestCase):
    def setUp(self):
        self.smote = SMOTE(k_neighbors=5)

    def test_smote(self):
        X = np.random.randint(0, 10, size=(33, 3))
        y = np.concatenate((np.zeros(3), np.ones(15), np.ones(15) * 2))
        n_majority = len(np.where(y == 2)[0])

        X_resampled, y_resampled = self.smote.fit_resample(X, y, 0, n_majority, N=100)

        self.assertEqual(X_resampled.shape, (45, 3))
        self.assertEqual(y_resampled.shape, (45,))


class SplitDataTestCase(TestCase):
    def test_split_data(self):
        X = np.random.randint(0, 10, size=(100, 3))
        y = np.array([0, 1, 2] * 100)
        X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2)

        self.assertEqual(X_train.shape[0], 80)
        self.assertEqual(y_train.shape[0], 80)
        self.assertEqual(X_test.shape[0], 20)
        self.assertEqual(y_test.shape[0], 20)


class AccuracyScoreTestCase(TestCase):
    def test_accuracy_score(self):
        y_true = np.array([0, 1, 2, 3, 4])
        y_pred = np.array([4, 3, 2, 1, 0])

        self.assertEqual(accuracy_score(y_true, y_pred), 0.2)
