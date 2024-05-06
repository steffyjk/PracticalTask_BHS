from django.db import models
import uuid

class Company(models.Model):
    """
        Company Model
        Id: UUID
        Name: String
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Employee(models.Model):
    """
        Employee Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    salary = models.IntegerField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        # [ Constain ] --> First name , Last name and company should be unique together
        unique_together = ['first_name', 'last_name', 'company']
