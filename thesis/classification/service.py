import random


class TextClassifier:
    def __init__(self) -> None:
        pass

    def predict(self, text: str) -> str:
        # TODO: developed model to predict
        class_name = ["Alus Singgih", "Alus Sor", "Andap/Kepara", "Kasar"]
        result = random.choice(class_name)
        return result
