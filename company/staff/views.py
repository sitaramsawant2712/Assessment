from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.views.generic import DetailView, ListView, CreateView


# Create your views here.
from .forms import EmployeeForm
from .models import Employee, Department


def index(request):
    context = {}
    return render(request, 'base.html', context=context)


class DepartmentListView(ListView):
    model = Department
    template_name = "staff/department_list.html"

    def get_queryset(self):
        return Department.objects.all()

    def  get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        return context


class DepartmentDetailView(DetailView):
    template_name = "staff/department_detail.html"
    model = Department

    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Department, id=_id)


class EmployeeListView(ListView):
    model = Employee
    template_name = "staff/employee_list.html"

    def get_queryset(self):
        return Employee.objects.all()

    def  get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        return context


class EmployeeDetailView(DetailView):
    template_name = "staff/employee_detail.html"
    model = Employee

    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Employee, id=_id)

    # def render_to_response(self, context, **kwargs):
    #     return FileResponse(self.object.picture)


class EmployeeCreateView(CreateView):
    template_name = 'staff/employee_create.html'
    form_class = EmployeeForm
    queryset = Employee.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
