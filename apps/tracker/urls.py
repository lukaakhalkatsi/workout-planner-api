from django.urls import path
from .views import WeightEntryListCreateView, FitnessGoalListCreateView

urlpatterns = [
    path('weights/', WeightEntryListCreateView.as_view(), name='weight-entry-list-create'),
    path('goals/', FitnessGoalListCreateView.as_view(), name='fitness-goal-list-create'),
]
