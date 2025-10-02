from django.urls import path
from .views import ExerciseListView, ExerciseDetailView

urlpatterns = [
    path('', ExerciseListView.as_view(), name='exercise-list'),
    path('<uuid:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),
]
