from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('employees/', views.employee_list, name='employees'),
    path('add/', views.add_employee, name='add_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance/', views.attendance_list, name='attendance'),
    path('api/employees/', views.employee_api),
    #path('api/employees/<int:id>/', views.delete_employee_api),
    path('api/attendance/', views.attendance_api),
]
