from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import WeightEntry, FitnessGoal
from .serializers import WeightEntrySerializer, FitnessGoalSerializer


class WeightEntryListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        entries = WeightEntry.objects.filter(user=request.user)
        serializer = WeightEntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = WeightEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FitnessGoalListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        goals = FitnessGoal.objects.filter(user=request.user)
        serializer = FitnessGoalSerializer(goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = FitnessGoalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

