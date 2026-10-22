
from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course_code", "course_name"]
        labels = {
            "course_code": "Course Code",
            "course_name": "Course Name",
        }
        widgets = {
            "course_code": forms.TextInput(
                attrs={"placeholder": "Enter course code"}
            ),
            "course_name": forms.TextInput(
                attrs={"placeholder": "Enter course name"}
            ),
        }
