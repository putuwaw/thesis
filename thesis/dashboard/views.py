from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, Page
from django.shortcuts import render
from classification.models import ClassificationReport
from .forms import CSVUploadForm

import pandas as pd


def _get_pagination_range(page_obj: Page):
    current_page = page_obj.number
    total_pages = page_obj.paginator.num_pages

    if total_pages <= 5:
        return list(range(1, total_pages + 1))
    elif total_pages > 5:
        if current_page <= 3:
            # Show first 4 pages and last page
            return list(range(1, 5)) + ["...", total_pages]
        elif current_page >= total_pages - 2:
            # Show first page, last 4 pages
            return [1, "..."] + list(range(total_pages - 3, total_pages + 1))
        else:
            # Show first page, 3 pages around the current page, and last page
            return (
                [1, "..."]
                + list(range(current_page - 1, current_page + 2))
                + ["...", total_pages]
            )


def _handle_form_submission(request: WSGIRequest, template_name: str):
    ctx = {}
    # file upload form
    if "submit_file_form" in request.POST:
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["file"]
            df = pd.read_csv(csv_file)
            print(df)
            return render(request, template_name, context=ctx)
        else:
            ctx = {
                "is_error": True,
                "errors": form.errors.as_data(),
            }
            return render(request, template_name, context=ctx)
    # normal form add new data
    if "submit_data_form" in request.POST:
        print(request.POST)
        return render(request, template_name, context=ctx)

    return render(request, template_name, context=ctx)


@login_required
def dashboard_home(request: WSGIRequest):
    # Get the current logged-in user's name
    username = request.user.username

    # get query parameter
    origin = request.GET.get("origin")

    ctx = {
        "username": username,
        "origin": origin,
    }
    return render(request, "dashboard/home.html", ctx)


@login_required
def dashboard_data(request: WSGIRequest):
    if request.method == "POST":
        return _handle_form_submission(request, "dashboard/data/all.html")
    return render(request, "dashboard/data/all.html")


@login_required
def dashboard_data_training(request: WSGIRequest):
    if request.method == "POST":
        return _handle_form_submission(request, "dashboard/data/training.html")
    return render(request, "dashboard/data/training.html")


@login_required
def dashboard_data_testing(request: WSGIRequest):
    if request.method == "POST":
        return _handle_form_submission(request, "dashboard/data/testing.html")
    return render(request, "dashboard/data/testing.html")


@login_required
def dashboard_training(request: WSGIRequest):
    return render(request, "dashboard/training.html")


@login_required
def dashboard_testing(request: WSGIRequest):
    return render(request, "dashboard/testing.html")


@login_required
def dashboard_report(request: WSGIRequest):
    reports_list = ClassificationReport.objects.order_by("-created_at").all()
    paginator = Paginator(reports_list, 10)
    page_number = request.GET.get("page", 1)
    page_obj: Page = paginator.page(page_number)
    pagination_list = _get_pagination_range(page_obj)

    ctx = {
        "page_obj": page_obj,
        "reports": page_obj.object_list,
        "show": {
            "start": page_obj.start_index(),
            "end": page_obj.end_index(),
            "range": list(range(page_obj.start_index(), page_obj.end_index() + 1)),
            "total_data": reports_list.count(),
            "previous": page_obj.has_previous(),
            "next": page_obj.has_next(),
        },
        "pagination_list": pagination_list,
    }
    return render(request, "dashboard/report.html", context=ctx)
