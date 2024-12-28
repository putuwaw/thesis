import json
from .models import ClassificationReport
from .service import TextClassifier
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def index(request: WSGIRequest):
    return render(request, "index.html")


def predict(request: WSGIRequest):
    if request.method == "POST":
        clf = TextClassifier()
        text: str = request.POST.get("text")
        prediction = clf.predict(text)
        ctx = {
            "prediction": True,
            "label": prediction[0],
            "probability": prediction[1],
            "fig": prediction[2],
            "info": prediction[3],
            "text": text,
            "categories_left": clf.categories_left,
        }
        return render(request, "predict.html", context=ctx)

    return render(request, "predict.html")


def about(request: WSGIRequest):
    return render(request, "about.html")


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
            return redirect("predict")
        except Exception as e:
            messages.error(request, f"Failed to submit report! {e}")
            return redirect("predict")


@csrf_exempt
def api_predict(request: WSGIRequest):
    if request.method == "POST":
        try:
            clf = TextClassifier()
            body = json.loads(request.body)
            text = body.get("text")
            if (not text) or (not isinstance(text, str)):
                return JsonResponse(
                    {
                        "status": False,
                        "message": "failed predict text",
                        "error": "text field is required and must be of type string",
                    },
                    status=400,
                )

            prediction = clf.predict(text)
            response = {
                "label": prediction[0],
                "probability": prediction[1],
            }
            return JsonResponse(
                {"status": True, "message": "success predict text", "data": response}
            )
        except Exception as e:
            return JsonResponse(
                {
                    "status": False,
                    "message": "failed predict text",
                    "error": str(e),
                },
                status=500,
            )
