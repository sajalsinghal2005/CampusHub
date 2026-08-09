from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return(
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )

class IsPlacement(BasePermission):
    def has_permission(self,request,view):
        return(
            request.user.is_authenticated
            and request.user.role =="PLACEMENT"
        )

class IsStudent(BasePermission):
    def has_permission(self,request,view):
        return(
            request.user.is_authenticated
            and request.user.role == "STUDENT"
        )

class IsPlacementOrAdmin(BasePermission):

    def has_permission(self,request,view):
        return(
            request.user.is_authenticated
            and request.user.role in ["PLACEMENT","ADMIN"]
        )
