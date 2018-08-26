from django.urls import path

from . import views

app_name = 'people'


urlpatterns = [
    # Clients
    path('client/', views.ClientListView.as_view(), name="client-list"),
    path('client/create/', views.ClientCreateView.as_view(), name="client-create"),
    path('client/<int:pk>/edit/', views.ClientUpdateView.as_view(), name="client-edit"),
    path('client/<int:pk>//detail/', views.ClientDetailView.as_view(), name="client-detail"),

    # Employees
    path('employee/', views.EmployeeListView.as_view(), name="employee-list"),
    path('employee/create/', views.EmployeeCreateView.as_view(), name="employee-create"),
    path('employee/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name="employee-edit"),
    path('employee/<int:pk>/detail/', views.EmployeeDetailView.as_view(), name="employee-detail"),
]
