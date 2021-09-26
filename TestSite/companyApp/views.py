from .serializers import CompanySerializer, EmployeeSerializer, CompanyListSerializer, EmployeeListSerializer

from .models import Company, Employee

from rest_framework.viewsets import GenericViewSet

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .core.mixins import SerializerMixin

from rest_framework.filters import OrderingFilter

from rest_framework.permissions import IsAuthenticated

class CompanyView(SerializerMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    serializers = {'list': CompanyListSerializer, 'create': CompanySerializer}
    queryset = Company.objects.all()
    filter_backends = (OrderingFilter,)
    permission_classes = (IsAuthenticated,)

class EmployeeView(SerializerMixin, ListModelMixin, CreateModelMixin ,GenericViewSet):
    serializers = {'list': EmployeeListSerializer, 'create': EmployeeSerializer}
    queryset = Employee.objects.all()
    filter_backends = (OrderingFilter,)
    permission_classes = (IsAuthenticated,)
