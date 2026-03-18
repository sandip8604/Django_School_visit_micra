from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import School, Visit
from .serializers import SchoolSerializer, VisitSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def dashboard(request):
    total_schools = School.objects.count()
    total_visits = Visit.objects.count()
    completed = Visit.objects.filter(status='done').count()
    pending = Visit.objects.filter(status='planned').count()

    return Response({
        "total_schools": total_schools,
        "total_visits": total_visits,
        "completed": completed,
        "pending": pending
    })