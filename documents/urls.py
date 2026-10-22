
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("documents/", views.documents_list, name="documents_list"),
    path("routing/", views.routing, name="routing"),
    path("approvals/", views.approvals, name="approvals"),
    path("releases/", views.releases, name="releases"),

    
    path("course/", views.course, name="course"),
    path("course/add/", views.course_create, name="course_create"),
    path("course/<int:pk>/edit/", views.course_update, name="course_update"),
    path("course/<int:pk>/delete/", views.course_delete, name="course_delete"),



]
