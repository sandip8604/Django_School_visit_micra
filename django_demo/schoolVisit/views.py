from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated,AllowAny

from schoolVisit.pagination import SchoolPagination

from .permission import IsStaffRole,IsAdminRole
from .models import School, Visit, User
from .serializers import SchoolSerializer, VisitSerializer, UserSerializer,SignupSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import  api_view,permission_classes
from rest_framework.views import  APIView

from rest_framework import generics

from rest_framework_simplejwt.tokens import RefreshToken


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated,IsStaffRole]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'city', 'principal']
    pagination_class = SchoolPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny] 

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsStaffRole]

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
     

        try:
            user = User.objects.get(username=username)
        
        except User.DoesNotExist:
            return Response({"error": "Invalid username"}, status=400)

        if not user.check_password(password):
            return Response({"error": "Invalid password"}, status=400)  

        refresh = RefreshToken.for_user(user)
        refresh['username'] = user.username
        refresh['role'] = user.role

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
        })
        
        
@api_view(['GET'])
@permission_classes([IsAdminRole])
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