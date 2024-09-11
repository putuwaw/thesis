from django.shortcuts import render

# Create your views here.
from django.core.handlers.wsgi import WSGIRequest
from .service import TextClassifier


def index(request: WSGIRequest):
    clf = TextClassifier()
    if request.method == "POST":
        text: str = request.POST.get("text")
        ctx = {
            "prediction": True,
            "label": clf.predict(text),
        }
        return render(request, "index.html", context=ctx)

    return render(request, "index.html")
