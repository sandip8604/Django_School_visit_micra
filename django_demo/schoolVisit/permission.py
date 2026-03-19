from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return (
        request.user and
        request.user.is_authenticated and          
        getattr(request.user, 'role', None) == 'admin'
        )



class IsStaffRole(BasePermission):
    def has_permission(self, request, view):
        
        print("===== Permission called =====")
        print("User:", request.user)

        return (
            request.user and
            request.user.is_authenticated and
            getattr(request.user, 'role', None) in ['admin', 'staff']
        )