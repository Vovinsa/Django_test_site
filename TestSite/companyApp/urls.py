from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('company/create/', CompanyView.as_view({'post': 'create'}), name='company_create'),
    path('employee/create/', EmployeeView.as_view({'post': 'create'}), name='employee_create'),
    path('company/list/', CompanyView.as_view({'get': 'list'}), name='company'),
    path('employee/list/', EmployeeView.as_view({'get': 'list'}), name='employee'),
    path('auth/', include('rest_framework.urls'))
]