from django.db import models

class Complaint(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        REVIEW = "review", "Needs review"
        RESOLVED = "resolved", "Resolved"

    class Priority(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"

    subject = models.CharField(max_length=180)
    description = models.TextField()
    predicted_category = models.CharField(max_length=80, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.LOW)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.NEW)
    requires_human_review = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.subject
