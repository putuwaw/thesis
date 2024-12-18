import os
import sys

from django.conf import settings

import joblib


class TextClassifier:
    def __init__(self) -> None:
        self.label_to_idx = {
            "Alus singgih": 0,
            "Alus sor": 1,
            "Alus mider": 2,
            "Alus madia": 3,
            "Basa andap": 4,
            "Basa kasar": 5,
        }
        self.idx_to_label = {v: k for k, v in self.label_to_idx.items()}
        self.categories_left = self.label_to_idx.keys()
        self.base_ml_path = os.path.join(settings.BASE_DIR, "classification/thesis_ml")
        self.pipeline = self._load_model(
            os.path.join(self.base_ml_path, "model/pipeline.joblib")
        )

    def _append_path(self, new_path) -> str:
        if new_path not in sys.path:
            sys.path.append(new_path)

    def _load_model(self, path: str):
        self._append_path(self.base_ml_path)

        return joblib.load(path)

    def predict(self, text: str) -> tuple[str, dict]:
        prediction = self.pipeline.predict(text)
        probability = self.pipeline.predict_proba(text)

        probability = probability[0]
        prob_result = {}
        for idx, prob in enumerate(probability):
            prob_result[self.idx_to_label[idx]] = round(float(prob) * 100, 2)

        result = self.idx_to_label[prediction]

        self.categories_left = [cat for cat in self.label_to_idx if cat != result]
        return result, prob_result
