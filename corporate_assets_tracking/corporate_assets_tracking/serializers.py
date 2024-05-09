from .models import Employee, Device, Assignment, Company
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
    