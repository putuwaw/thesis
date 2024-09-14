from .models import ClassificationReport
from .service import TextClassifier
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.utils import timezone


def index(request: WSGIRequest):
    if request.method == "POST":
        clf = TextClassifier()
        text: str = request.POST.get("text")
        ctx = {
            "prediction": True,
            "label": clf.predict(text),
            "text": text,
            "categories_left": clf.categories_left,
        }
        return render(request, "index.html", context=ctx)

    return render(request, "index.html")


def report(request: WSGIRequest):
    if request.method == "POST":
        try:
            predicted_text = request.POST.get("predicted_text")
            predicted_class = request.POST.get("predicted_class")
            expected_class = request.POST.get("expected_class")

            report = ClassificationReport(
                predicted_text=predicted_text,
                predicted_class=predicted_class,
                expected_class=expected_class,
                created_at=timezone.now(),
            )
            report.save()
            messages.success(request, "Report submitted successfully!")
            return redirect("index")
        except Exception as e:
            messages.error(request, f"Failed to submit report! {e}")
            return redirect("index")
