from django.forms import forms, ModelForm
from .models import StudentDetails

class StudentDetailsForm(ModelForm):
    class Meta:
        models = StudentDetails
        fields = "__all__"