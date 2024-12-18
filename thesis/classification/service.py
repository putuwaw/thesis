import os
import sys

from django.conf import settings

import joblib
import plotly.graph_objects as go


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
        # TODO: normalize text
        # TODO: short probability

        prediction = self.pipeline.predict(text)
        probability = self.pipeline.predict_proba(text)

        probability = probability[0]
        prob_result = {}
        for idx, prob in enumerate(probability):
            prob_result[self.idx_to_label[idx]] = round(float(prob) * 100, 2)

        # table
        sorted_prob_result = dict(
            sorted(prob_result.items(), key=lambda item: item[1], reverse=True)
        )
        # prediction
        result = self.idx_to_label[prediction]

        sorted_prob_result_asc = dict(
            sorted(prob_result.items(), key=lambda item: item[1])
        )
        fig = go.Figure(
            go.Bar(
                x=list(sorted_prob_result_asc.values()),
                y=list(sorted_prob_result_asc.keys()),
                orientation="h",
                marker=dict(color="green"),
                text=list(sorted_prob_result_asc.values()),
            )
        )

        fig.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            xaxis=dict(showticklabels=False),
            yaxis=dict(showticklabels=True),
            margin=dict(l=10, r=10, t=10, b=10),
        )

        self.categories_left = [cat for cat in self.label_to_idx if cat != result]
        return result, sorted_prob_result, fig.to_html(full_html=False)
