import pandas as pd

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

class ImportData(CreateAPIView):

    def post(self, request, *args, **kwargs):
        df = pd.read_excel('source\Practical Task Python sheet (4).xlsx', engine='openpyxl')
        return Response("Data Imported Successfully!", status=status.HTTP_200_OK)



