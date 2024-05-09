"""
URL configuration for corporate_assets_tracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import CompanyList, CompanyDetails, EmployeeList, EmployeeDetails, DeviceList, DeviceDetails, AssignmentList, AssignmentDetails
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title = "Asset Tracking API")

urlpatterns = [
    
    path('company/', CompanyList.as_view(), name='comapny-list'),
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company-details'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetails.as_view(), name='employee-details'),
    path('device/', DeviceList.as_view(), name='device-list'),
    path('device/<int:pk>/', DeviceDetails.as_view(), name='device-details'),
    path('assignment/', AssignmentList.as_view(), name='assignment-list'),
    path('assignment/<int:pk>/', AssignmentDetails.as_view(), name='assignment-details'),
    path('swagger-docs/', schema_view) ,
]
