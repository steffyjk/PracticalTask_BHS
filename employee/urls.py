from django.urls import path
from .views import ImportData, EmployeeListView


urlpatterns = [
    # URL pattern for importing data
    path('import-data/', ImportData.as_view(), name='import-data'),

    # URL pattern for displaying a list of employees
    path('', EmployeeListView.as_view(), name='employee_list'),
]
