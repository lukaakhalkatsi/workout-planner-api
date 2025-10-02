from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import WorkoutPlan, WorkoutExercise
from .serializers import WorkoutPlanSerializer, WorkoutExerciseSerializer

@extend_schema(
    tags=['Workouts'],
    responses=WorkoutPlanSerializer(many=True),
    request=WorkoutPlanSerializer
)
class WorkoutPlanListCreateView(APIView):
    """
    GET: List all workout plans of the authenticated user.
    POST: Create a new workout plan with exercises.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        plans = WorkoutPlan.objects.filter(user=request.user)
        serializer = WorkoutPlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id  # attach the authenticated user
        serializer = WorkoutPlanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Workouts'],
    responses=WorkoutPlanSerializer,
    request=WorkoutPlanSerializer
)
class WorkoutPlanDetailView(APIView):
    """
    GET: Retrieve a specific workout plan by ID.
    PUT: Update a workout plan and its exercises.
    DELETE: Delete a workout plan.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return WorkoutPlan.objects.prefetch_related('exercises__exercise').get(pk=pk, user=user)
        except WorkoutPlan.DoesNotExist:
            return None

    def get(self, request, pk):
        plan = self.get_object(pk, request.user)
        if not plan:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutPlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, pk):
        plan = self.get_object(pk, request.user)
        if not plan:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = WorkoutPlanSerializer(plan, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        plan = self.get_object(pk, request.user)
        if not plan:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
