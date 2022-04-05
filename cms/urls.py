from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),


    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
   
    path('tasks/', views.tasks, name="tasks"),
    path('task/<pk>/', views.taskDetail, name="task"),
    path('tasks-completed/', views.tasksCompleted, name="tasks-completed"),
    path('tasks-due/', views.tasksDue, name="tasks-due"),
    path('add-task/', views.addTask, name="add-task"),
    path('edit-task/<pk>', views.editTask, name="edit-task"),
    path('complete-task/<pk>/', views.completeTask, name="complete-task"),
    path('delete-task/<pk>', views.deleteTask, name="delete-task"),


    path('employee-settings/', views.emplyeeSettings, name="employee-settings"),
    path('employees/', views.employees, name="employees"),
    path('add-employee/', views.addEmployee, name="add-employee"),


    path('clients/', views.clients, name="clients"),
    path('clients/', views.clients, name="clients"),
    path('clients-website/', views.clientsWebsite, name="clients-website"),
    path('clients-sociale-media/', views.clientsSocialMedia, name="clients-sociale-media"),
    path('clients-content/', views.clientsContent, name="clients-content"),

    path('activities/', views.activities, name="activities"),
    path('add-activity/', views.addActivity, name="add-activity"),
    path('complete-activity/<pk>/', views.completeActivity, name="complete-activity"),
    path('delete-activity/<pk>/', views.deleteActivity, name="delete-activity"),



]