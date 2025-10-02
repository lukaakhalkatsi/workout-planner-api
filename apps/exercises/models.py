from django.db import models

from apps.base.models import BaseModel


class Exercise(BaseModel):
    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text="Detailed description of the exercise")
    instructions = models.TextField(help_text="Step-by-step instructions for execution")
    target_muscles = models.CharField(max_length=200, help_text="Primary muscles worked, comma-separated")
    equipment = models.CharField(max_length=100, blank=True, null=True, help_text="Equipment needed, if any")
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default='Beginner')
    duration_seconds = models.PositiveIntegerField(blank=True, null=True, help_text="Optional default duration in seconds")
    distance_meters = models.PositiveIntegerField(blank=True, null=True, help_text="Optional distance in meters, for cardio exercises")

    class Meta:
        ordering = ['name']
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.name

