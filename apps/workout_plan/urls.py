from django.urls import path
from .views import WorkoutPlanListCreateView, WorkoutPlanDetailView

urlpatterns = [
    path('plans/', WorkoutPlanListCreateView.as_view(), name='workoutplan-list-create'),
    path('plans/<uuid:pk>/', WorkoutPlanDetailView.as_view(), name='workoutplan-detail'),
]
