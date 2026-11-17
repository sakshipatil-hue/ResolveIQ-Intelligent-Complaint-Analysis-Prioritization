from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from .forms import ComplaintForm
from .models import Complaint
from .services.analysis import analyze_complaint

def dashboard(request):
    complaints = Complaint.objects.all()[:8]
    total = Complaint.objects.count()
    high = Complaint.objects.filter(priority=Complaint.Priority.HIGH).count()
    review = Complaint.objects.filter(requires_human_review=True).count()
    resolved = Complaint.objects.filter(status=Complaint.Status.RESOLVED).count()
    categories = (Complaint.objects.exclude(predicted_category="")
                 .values("predicted_category").annotate(count=Count("id")).order_by("-count")[:6])
    return render(request, "complaints/dashboard.html", {
        "complaints": complaints, "total": total, "high": high,
        "review": review, "resolved": resolved, "categories": categories,
    })

def create_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            result = analyze_complaint(complaint.description)
            complaint.predicted_category = result["category"]
            complaint.confidence = result["confidence"]
            complaint.priority = result["priority"]
            complaint.requires_human_review = result["requires_human_review"]
            complaint.save()
            return redirect("complaints:detail", pk=complaint.pk)
    else:
        form = ComplaintForm()
    return render(request, "complaints/create.html", {"form": form})

def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, "complaints/detail.html", {"complaint": complaint})
