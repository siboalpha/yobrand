from ast import Return
from genericpath import exists
from multiprocessing import context
from tokenize import group
from unicodedata import name
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, managers_only


# Create your views here.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        emplyoyee = authenticate(request, username=username,password=password)
        if emplyoyee is not None:
            login(request,emplyoyee)
            return redirect('dashboard')
    context = {}
    return render(request, 'cms/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = CreateEmployeeForm()
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        user = form.save()
        group = Group.objects.get(name='employees')
        user.groups.add(group)
        return redirect('login')
    context = {'form':form}
    return render(request, 'cms/register.html', context)




@login_required(login_url='login')
@managers_only
def dashboard(request):
    tasks = Task.objects.all().order_by('due_date', 'due_time')
    task_count = Task.objects.all().count()
    uncompleted_task_task_count = Task.objects.filter(complete = False).count()
    if task_count == 0:
        value = (uncompleted_task_task_count * 100)/1
        x = 0
        y = 0
    else:
        value = (uncompleted_task_task_count * 100)/task_count
        formatted_value = "{:.2f}".format(value)
        x=float(formatted_value)
        y = 100-x
    
    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    requests = EmployeeRequest.objects.all()
    requests_notification = EmployeeRequest.objects.all().count
    context = {'tasks': tasks, 'task_count': task_count, 'x': x, 'y': y,'requests': requests, 'tasks_notification':tasks_notification, 'requests_notification': requests_notification}
    print(task_count)
    return render(request, 'cms/dashboard.html', context)




@login_required(login_url='login')
def tasks(request):
    tasks = Task.objects.filter(employee=request.user).order_by('due_date', 'due_time')
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'tasks': tasks, 'tasks_notification': tasks_notification}
    return render(request, 'cms/tasks.html', context)


@login_required(login_url='login')
def tasksCompleted(request):
    tasks = Task.objects.filter(employee=request.user)
    tasks_count = tasks.filter(complete = False ).count()

    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'tasks': tasks, 'tasks_notification': tasks_notification}
    return render(request, 'cms/tasks-completed.html', context)


@login_required(login_url='login')
def tasksDue(request):
    tasks = request.user.task_set.all()

    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'tasks': tasks, 'tasks_notification': tasks_notification}
    return render(request, 'cms/tasks-due.html', context)


@login_required(login_url='login')
def addTask(request):
    form = AddTaskForm()
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()

    context = {'form':form, 'tasks_notification': tasks_notification}
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    return render(request, 'cms/add-task.html', context)

def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = AddTaskForm(instance=task)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'cms/edit-task.html', context)

def taskDetail(request, pk):
    task = Task.objects.get(id=pk)

    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'task': task, 'tasks_notification': tasks_notification}
    return render(request, 'cms/task.html', context)


@login_required
def completeTask(request,pk):
   task = Task.objects.get(id=pk)
   task.complete = True
   task.save()
   return redirect('dashboard')


@login_required
def deleteTask(request,pk):
   task = Task.objects.get(id=pk)
   task.delete()
   return redirect('dashboard')





@login_required(login_url='login')
def clients(request):
    client_list = Client.objects.all()
    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'client_list':client_list, 'tasks_notification' :tasks_notification}
    return render(request, 'cms/clients.html', context)


@login_required(login_url='login')
def clientsWebsite(request):

    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'tasks_notification':tasks_notification}
    return render(request, 'cms/clients-website.html', context)


@login_required(login_url='login')
def clientsSocialMedia(request):

    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'tasks_notification': tasks_notification}
    return render(request, 'cms/clients-sociale-media.html', context)


@login_required(login_url='login')
def clientsContent(request):

    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'tasks_notification': tasks_notification}
    return render(request, 'cms/clients-content.html', context)





@login_required(login_url='login')
def activities(request):
    activities = Activity.objects.all()

    #Notification count
    tasks_notification = Task.objects.filter(employee=request.user, complete = False).count()
    context = {'activities': activities, 'tasks_notification' :tasks_notification}
    return render(request, 'cms/activities.html', context)

@login_required(login_url='login')
def addActivity(request):
    form = AddActivityForm()
    context = {'form':form}
    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            user_request = form.save(commit=False)
            user_request.author = request.user
            form.save()
            return redirect('activities')
        else:
            form = AddActivityForm()
    return render(request, 'cms/add-activity.html', context)


def completeActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    activity.complete = True
    activity.save()
    return redirect('activities')

def deleteActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    activity.delete()
    return redirect('activities')


def employees(request):
    employees_list = Employee.objects.all()
    context = {'employees_list': employees_list}
    return render(request, 'cms/employees.html', context)

def addEmployee(request):
    form = EmployeeForm()
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    return render(request, 'cms/add-employee.html', context)

def emplyeeSettings(request, pk):
    employee = request.user
    form = EmployeeForm(id=pk, instance=employee)
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'cms/employee-settings.html', context)


def submitRequest(request):
    form = SubmitRequest()
    if request.method == 'POST':
        form = SubmitRequest(request.POST)
        if form.is_valid():
            submited_request = form.save(commit=False)
            submited_request.from_user = request.user
            form.save()
            return redirect('dashboard')
        else:
            form = SubmitRequest()
    context = {'form':form}
    return render(request, 'cms/submi-request.html', context)

    