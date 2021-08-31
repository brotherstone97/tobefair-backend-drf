from django.shortcuts import render

from .models import Branch
from .serializers import BranchSerializer
from rest_framework import viewsets


class Branches_view_set(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
