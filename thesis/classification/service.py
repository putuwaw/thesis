import random


class TextClassifier:
    def __init__(self) -> None:
        self.categories = ["Alus Singgih", "Alus Sor", "Andap/Kepara", "Kasar"]
        self.categories_left = self.categories

    def predict(self, text: str) -> str:
        # TODO: developed model to predict
        result = random.choice(self.categories)

        self.categories_left = [cat for cat in self.categories if cat != result]
        return result
