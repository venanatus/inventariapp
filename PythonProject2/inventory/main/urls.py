from django.urls import path
from .views import ItemAPIList, ItemAPIDetail, DepartmentAPIList, DepartmentAPIDetail

urlpatterns = [
    # Items
    path('items/', ItemAPIList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemAPIDetail.as_view(), name='item-detail'),

    # Departments
    path('departments/', DepartmentAPIList.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentAPIDetail.as_view(), name='department-detail'),
]
