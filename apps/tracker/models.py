from django.db import models
from django.contrib.auth.models import User
from apps.base.models import BaseModel

class WeightEntry(BaseModel):
    """
    Tracks a user's weight over time.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_entries')
    date = models.DateField()
    weight_kg = models.FloatField()

    class Meta:
        ordering = ['-date']  # latest first

    def __str__(self):
        return f"{self.user.username}: {self.weight_kg}kg on {self.date}"

class FitnessGoal(BaseModel):
    """
    Represents a user's fitness goal.
    Can be weight-based or exercise-specific.
    """
    GOAL_TYPE_CHOICES = [
        ('weight', 'Weight'),
        ('exercise', 'Exercise'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fitness_goals')
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPE_CHOICES)
    target_value = models.FloatField(help_text="Target weight (kg) or exercise metric")
    exercise = models.ForeignKey('exercises.Exercise', null=True, blank=True, on_delete=models.SET_NULL)
    deadline = models.DateField(null=True, blank=True)
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} goal: {self.goal_type} - {self.target_value}"
