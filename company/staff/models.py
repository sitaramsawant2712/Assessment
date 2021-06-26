from django.db import models
from django.urls import reverse

# Create your models here.

class BaseModel(models.Model):
    """
    BaseModel (Abstract model for create and modified datetime)

    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    class Meta:
        db_table = "department"
        verbose_name = "department"
        verbose_name_plural = "department"

    def get_absolute_url(self):
        return reverse("department-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name


class Employee(BaseModel):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, related_name='employee_department', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    date_of_birth = models.DateField(max_length=8)
    picture = models.FileField(upload_to='upload/', blank=True, null=True)

    class Meta:
        db_table = "employee"
        verbose_name = "employee"
        verbose_name_plural = "employee"

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name


'''
Employee name
Department
Email
Date of birth
Picture
Department table
Department name
Manager (employee)

'''