import pandas as pd
from.serializers import EmployeeSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

class ImportData(CreateAPIView):

    def post(self, request, *args, **kwargs):
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
            return Response("Data Imported Successfully!", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



