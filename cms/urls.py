from django.urls import path, include
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

    path('user-settings/<pk>', views.userSettings, name="user-settings"),
    path('employees/', views.employees, name="employees"),
    path('add-employee/', views.addEmployee, name="add-employee"),
    path('employee-profile/<pk>', views.employeeProfile, name='employee-profile'),
    path('edit-employee/<pk>', views.editEmployee, name='edit-employee'),

    path('clients/', views.clients, name="clients"),
    path('add-client/', views.addClient, name='add-client'),
    path('edit-client/<pk>/', views.editClient, name="edit-client"),
    path('delete-client/<pk>', views.deleteClient, name='delete-client'),
    path('client-profile/<pk>/', views.clientProfile, name="client-profile"),

    path('activities/', views.activities, name="activities"),
    path('add-activity/', views.addActivity, name="add-activity"),
    path('complete-activity/<pk>/', views.completeActivity, name="complete-activity"),
    path('delete-activity/<pk>/', views.deleteActivity, name="delete-activity"),

    path('user-request/<pk>/', views.userRequest, name='user-request'),
    path('submit-request/', views.submitRequest, name='submit-request'),
    path('resolve-request/<pk>/', views.resolveRequest, name='resolve-request'),
    path('delete-request/<pk>/', views.deleteRequest, name='delete-request'),
    path('user-requests/', views.userRequests, name="user-requests"),

    path('projects/',views.projects, name='projects'),
    path('project/<pk>/',views.project, name='project'),
    path('add-project/', views.addProject, name='add-project'),
    path('delete-project/<pk>', views.deleteProject, name='delete-project'),
    path('edit-project/<pk>', views.editProject, name='edit-project'),
    path('complete-project/<pk>', views.completeProject, name='complete-project'),
    path('uncomplete-project/<pk>', views.uncompleteProject, name='uncomplete-project')
]