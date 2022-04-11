from django.contrib import admin
from .models import Client, Project, Task, Activity, Employee, EmployeeRequest

# Register your models here.

admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Activity)
admin.site.register(EmployeeRequest)