from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company

class CompanyTests(TestCase):
    

    def test_get_companies_list(self):
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_company(self):
        url = reverse('company-list')
        data = {'name': 'New Company'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)

    def test_get_company_detail(self):
        url = reverse('company-detail', kwargs={'pk': self.company.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.company.name)

