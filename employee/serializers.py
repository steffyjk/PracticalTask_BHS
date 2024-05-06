from rest_framework import serializers
from .models import Employee, Company

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company__name')

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'salary', 'manager_id', 'department_id', 'company_name', 'employee_id']

    def create(self, validated_data):
        company_name = validated_data.pop('company__name')
        company, _ = Company.objects.get_or_create(name=company_name)
        employee = Employee.objects.create(company=company, **validated_data)
        return employee
