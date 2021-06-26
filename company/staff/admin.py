from django.contrib import admin

# Register your models here.
from .models import Employee, Department


class EmployeeAdmin(admin.ModelAdmin):
    # list to display
    list_display = ('name', 'department', 'date_of_birth')
    # list filter
    list_filter = ('department__name', 'date_of_birth')
    # remove action
    actions = None


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Employees'


class DepartmentAdmin(admin.ModelAdmin):
    inlines = (EmployeeInline,)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
