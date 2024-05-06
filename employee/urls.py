from django.urls import path
from .views import ImportData

# Various url patterns for calling APIs
urlpatterns = [
    path('import-data/', ImportData.as_view(), name='import-data'),
]
