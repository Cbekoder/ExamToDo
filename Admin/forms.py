from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = "__all__"
