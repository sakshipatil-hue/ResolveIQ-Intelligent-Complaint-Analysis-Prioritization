from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["subject", "description"]
        widgets = {
            "subject": forms.TextInput(attrs={"placeholder": "Briefly describe the issue"}),
            "description": forms.Textarea(attrs={"placeholder": "Explain what happened...", "rows": 7}),
        }
