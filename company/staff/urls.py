from django.urls import path
from .views import index, EmployeeListView, EmployeeCreateView, EmployeeDetailView, DepartmentListView, DepartmentDetailView

urlpatterns = [
    path('', index, name='index'),
    path('employee/', EmployeeListView.as_view(), name='employee'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:id>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('department/', DepartmentListView.as_view(), name='department' ),
    path('department/<int:id>/', DepartmentDetailView.as_view(), name='department-detail'),
]