from django.urls import path
from . import views

app_name = "complaints"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("new/", views.create_complaint, name="create"),
    path("complaints/<int:pk>/", views.complaint_detail, name="detail"),
]
