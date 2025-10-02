from django.db import models
from apps.exercises.models import Exercise
from apps.base.models import BaseModel
from config.settings import AUTH_USER_MODEL


class WorkoutPlan(BaseModel):
    """
    Represents a personalized workout plan created by a user.
    Users can specify goals, plan type, frequency, and daily session duration.
    """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workout_plans")
    name = models.CharField(max_length=150)
    goal = models.CharField(max_length=100, help_text="User's fitness goal for this plan (e.g., 'Build muscle', 'Lose weight').")
    plan_type = models.CharField(max_length=50, help_text="Type of plan (e.g., 'Strength', 'Cardio', 'Mixed').")
    daily_session_duration = models.PositiveIntegerField(null=True, blank=True, help_text="Recommended duration of daily workout sessions in minutes.")
    frequency_per_week = models.PositiveIntegerField(help_text="Number of workout days per week.")

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class WorkoutExercise(BaseModel):
    """
    Represents a specific exercise assigned to a workout plan.
    Users can customize repetitions, sets, duration, or distance for each exercise.
    """
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name="exercises")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField(null=True, blank=True)
    sets = models.PositiveIntegerField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True, help_text="Duration in minutes for timed exercises.")
    distance_meters = models.PositiveIntegerField(null=True, blank=True, help_text="Distance in meters for exercises like running, cycling, or swimming.")

    def __str__(self):
        return f"{self.exercise.name} in {self.workout_plan.name}"
