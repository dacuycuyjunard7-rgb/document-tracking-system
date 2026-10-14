
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("documents/", views.documents_list, name="documents_list"),
    path("routing/", views.routing, name="routing"),
    path("approvals/", views.approvals, name="approvals"),
    path("releases/", views.releases, name="releases"),


]
