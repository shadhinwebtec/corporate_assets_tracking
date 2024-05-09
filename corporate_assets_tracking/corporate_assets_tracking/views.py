from rest_framework import generics
from .models import Company, Employee, Device, Assignment 
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, AssignmentSerializer 

# PhoneCompany Views
# class PhoneCompanyList(generics.ListCreateAPIView):
#     queryset = PhoneCompany.objects.all()
#     serializer_class = PhoneCompanySerializer


# Company views
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# Employee Views
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Device Views
class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# Assignment Views
class AssignmentList(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer