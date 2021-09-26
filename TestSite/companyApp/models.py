from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    companies = models.ManyToManyField('self', blank=True)
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    @property
    def num_employee(self):
        return self.app_employee.count()

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.surname
