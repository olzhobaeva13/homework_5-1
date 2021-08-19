from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Employee
from django.shortcuts import get_object_or_404

class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employees/employees_list.html', context={'employees': employees})

class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employees/employee_detail.html'

