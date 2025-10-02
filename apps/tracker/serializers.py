from rest_framework import serializers
from .models import WeightEntry, FitnessGoal

class WeightEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightEntry
        fields = ['id', 'date', 'weight_kg']

class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = ['id', 'goal_type', 'target_value', 'exercise', 'deadline', 'achieved']
