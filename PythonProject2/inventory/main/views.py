# from django.shortcuts import render
# from rest_framework import generics
# from .models import Item, Department
#
# from .serializers import ItemSerializer, DepartmentSerializer
#
#
# class ItemAPIList(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
# class DepartmentAPIList(generics.ListCreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#
#
#

from django.shortcuts import render
from rest_framework import generics
from .models import Item, Department
from .serializers import ItemSerializer, DepartmentSerializer


# Item Views
class ItemAPIList(generics.ListCreateAPIView):
    """View для отображения списка и создания новых объектов Item."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    """View для получения, обновления и удаления конкретного объекта Item."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Department Views
class DepartmentAPIList(generics.ListCreateAPIView):
    """View для отображения списка и создания новых объектов Department."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    """View для получения, обновления и удаления конкретного объекта Department."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
