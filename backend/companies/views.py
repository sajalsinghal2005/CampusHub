from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Company
from .serializers import CompanySerializer
from accounts.permissions import IsPlacementOrAdmin


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method=="POST":
            return [IsPlacementOrAdmin()]
        return [IsAuthenticated]

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method in ["PUT","PATCH","DELETE"]:
            return [IsPlacementOrAdmin()]
        return [IsAuthenticated()]