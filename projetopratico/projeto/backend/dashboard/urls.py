from django.urls import path
from .views import DashboardView, RegisterRequestView

urlpatterns = [
    path('dashboard/', DashboardView.as_view()),
    path('request/', RegisterRequestView.as_view())
]