from django.shortcuts import render
from rest_framework import viewsets
from categories.serializers import CategorySerializer
from categories.models import Category
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
