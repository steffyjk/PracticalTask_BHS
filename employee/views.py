import pandas as pd
from.serializers import EmployeeSerializer
from rest_framework.generics import CreateAPIView
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import status
from core.utils import response_body
from .models import Employee

class ImportData(CreateAPIView):
    """
    API endpoint to import data from an Excel file into the Employee model.

    Methods:
    - post(self, request, *args, **kwargs): Handles the POST request to import data.
    """

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request to import data from an Excel file.

        Args:
        - request: HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: HTTP response with import status.
        """
        try:  
            df = pd.read_excel('source\Practical Task Python sheet (4).xlsx', engine='openpyxl')

            # Converting the title of the columns as per needed in Django Model
            df = df.rename(columns={'EMPLOYEE_ID': 'employee_id', 'FIRST_NAME': 'first_name', 'LAST_NAME': 'last_name',
                                    'PHONE_NUMBER': 'phone_number', 'COMPANY_NAME': 'company_name', 
                                    'SALARY': 'salary', 'MANAGER_ID': 'manager_id', 'DEPARTMENT_ID': 'department_id'})

            # Converting Dataframe to dictionary to serialize
            data_dict = df.to_dict(orient='records')

            serializer = EmployeeSerializer(data=data_dict, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(response_body(status.HTTP_200_OK, message="Data Imported Successfully!"))
            else:
                return Response(response_body(status.HTTP_400_BAD_REQUEST, errors=serializer.errors))
        
        except Exception as err:
            # Handle any exceptions and return an appropriate error response
            return Response(response_body(status.HTTP_500_INTERNAL_SERVER_ERROR, errors=str(err)))


class EmployeeListView(ListView):
    """
    View to display a list of employees.

    Attributes:
    - model: Specifies the model to be used for the ListView.
    - template_name: Specifies the template file used to render the view.
    - context_object_name: Specifies the name of the variable containing the list of employees in the template context.
    """

    model = Employee
    template_name = 'employee_list.html'  
    context_object_name = 'employees'