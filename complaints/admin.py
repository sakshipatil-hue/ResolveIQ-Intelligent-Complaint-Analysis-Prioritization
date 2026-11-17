from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("subject", "predicted_category", "priority", "status", "confidence", "created_at")
    list_filter = ("priority", "status", "predicted_category")
    search_fields = ("subject", "description")
