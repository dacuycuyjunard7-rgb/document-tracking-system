from django.contrib.auth.decorators import login_required

from django.shortcuts import render

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

