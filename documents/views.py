from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm


@login_required
def dashboard(request):
    return render(request, "documents/dashboard.html")


def documents_list(request):
    return render(request, "documents/documents_list.html")


def routing(request):
    return render(request, "documents/routing.html")


def approvals(request):
    return render(request, "documents/approvals.html")


def releases(request):
    return render(request, "documents/releases.html")


def course(request):
    course_list = Course.objects.all().order_by("course_code")
    return render(
        request,
        "documents/course.html",
        {"courses": course_list}
    )


def course_create(request):
    form = CourseForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("course")

    return render(
        request,
        "documents/course_form.html",
        {"form": form, "title": "Add Course"}
    )


def course_update(request, pk):
    course_item = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course_item)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("course")

    return render(
        request,
        "documents/course_form.html",
        {"form": form, "title": "Edit Course"}
    )


def course_delete(request, pk):
    course_item = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        course_item.delete()
        return redirect("course")

    return render(
        request,
        "documents/course_confirm_delete.html",
        {"course": course_item}
    )

