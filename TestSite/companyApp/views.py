from rest_framework.viewsets import GenericViewSet

from rest_framework.mixins import ListModelMixin, CreateModelMixin

from django_filters import rest_framework as filters

from rest_framework.permissions import IsAuthenticated

from .serializers import CompanySerializer, EmployeeSerializer, CompanyListSerializer, EmployeeListSerializer

from .models import Company, Employee

from .core.mixins import SerializerMixin

class CompanyView(SerializerMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    serializers = {'list': CompanyListSerializer, 'create': CompanySerializer}
    queryset = Company.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('companies')
    permission_classes = (IsAuthenticated,)

class EmployeeView(SerializerMixin, ListModelMixin, CreateModelMixin ,GenericViewSet):
    serializers = {'list': EmployeeListSerializer, 'create': EmployeeSerializer}
    queryset = Employee.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name')
    permission_classes = (IsAuthenticated,)
