from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Exercise
from .serializers import ExerciseSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Exercises'])
class ExerciseListView(APIView):
    """
    GET /api/exercises/
    Returns a list of all predefined exercises.
    """

    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=['Exercises'])
class ExerciseDetailView(APIView):
    """
    GET /api/exercises/{id}/
    Returns detailed information for a specific exercise.
    """

    def get(self, request, pk):
        try:
            exercise = Exercise.objects.get(pk=pk)
        except Exercise.DoesNotExist:
            return Response({"detail": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data, status=status.HTTP_200_OK)
