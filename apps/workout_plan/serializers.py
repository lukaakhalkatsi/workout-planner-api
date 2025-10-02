from rest_framework import serializers
from .models import WorkoutPlan, WorkoutExercise
from apps.exercises.models import Exercise


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'repetitions', 'sets', 'duration_minutes', 'distance_meters']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'goal', 'plan_type', 'daily_session_duration', 'frequency_per_week', 'exercises']

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        plan = WorkoutPlan.objects.create(**validated_data)
        for exercise_data in exercises_data:
            WorkoutExercise.objects.create(workout_plan=plan, **exercise_data)
        return plan
