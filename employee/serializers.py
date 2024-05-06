from rest_framework import serializers
from .models import Employee, Company

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model.
    
    This serializer is responsible for serializing and deserializing Employee objects.
    It includes the company name as a read-only field and handles creating new Employee instances.

    Attributes:
        company_name: A CharField representing the name of the associated company.
        
    Methods:
        create: Overrides the create method to handle creating new Employee instances,
                ensuring that the associated company is retrieved or created.
    """

    company_name = serializers.CharField(source='company__name')

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'salary', 'manager_id', 'department_id', 'company_name', 'employee_id']

    def create(self, validated_data):
        """
        Create method for handling the creation of new Employee instances.
        
        This method overrides the default create method to ensure that the associated company 
        is retrieved or created based on the provided company name before creating the Employee instance.
        
        Args:
            validated_data (dict): The validated data used to create the Employee instance.
        
        Returns:
            Employee: The newly created Employee instance.
        """
        company_name = validated_data.pop('company__name')
        company, _ = Company.objects.get_or_create(name=company_name)
        employee = Employee.objects.create(company=company, **validated_data)
        return employee
