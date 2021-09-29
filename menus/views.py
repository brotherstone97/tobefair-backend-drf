from django.shortcuts import render

from .models import Ingredient, Menu
from .serializers import IngredientSerializer, MenuSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class Menus_view_set(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class Ingredients_view_set(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
