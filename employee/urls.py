from django.urls import path
from .views import ImportData, EmployeeListView

# Various url patterns for calling APIs
urlpatterns = [
    path('import-data/', ImportData.as_view(), name='import-data'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
]  