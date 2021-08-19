from django.urls import path
from .views import EmployeeView, EmployeeDetailView

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee_list_url'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail_url')
]