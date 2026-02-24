
from django.contrib.auth.decorators import login_required



##@login_required
##def dashboard(request):
##    return render(request, 'dashboard.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Attendance
from .forms import EmployeeForm, AttendanceForm
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer, AttendanceSerializer
from .models import Employee, Attendance
from datetime import date, timedelta
from django.shortcuts import render
from .models import Employee, Attendance

def home(request):
    return render(request, 'home.html')
@login_required
def dashboard(request):
    employee_count = Employee.objects.count()
    present_today = Attendance.objects.filter(date=date.today(), status="Present").count()
    absent_today = Attendance.objects.filter(date=date.today(), status="Absent").count()
    unmarked=employee_count-present_today-absent_today
    return render(request, 'dashboard.html', {
        'employee_count': employee_count,
        'present_today': present_today,
        'absent_today': absent_today,
        'unmarked_employee_today':unmarked,
    })


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, "Employee added successfully")
            return redirect('employees')
        except:
            messages.error(request, "Duplicate Employee ID or Email")
    return render(request, 'add_employee.html', {'form': form})

def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('employees')

def mark_attendance(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, "Attendance marked")
            return redirect('attendance')
        except:
            messages.error(request, "Attendance already marked for this date")
    return render(request, 'mark_attendance.html', {'form': form})

def attendance_list(request):
    records = Attendance.objects.select_related('employee').all()
    return render(request, 'attendance.html', {'records': records})

@api_view(['GET', 'POST'])
def employee_api(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##@api_view(['DELETE'])
##def delete_employee_api(request, id):
##    try:
##        employee = Employee.objects.get(id=id)
##    except Employee.DoesNotExist:
##        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
##
##    employee.delete()
##    return Response({"message": "Employee deleted"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def attendance_api(request):
    if request.method == 'GET':
        records = Attendance.objects.all()
        serializer = AttendanceSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def attendance_list(request):
    employees = Employee.objects.all()
    records = Attendance.objects.all()

    start_date = date(2026, 1, 1)   
    end_date = date.today()

    date_list = []
    current = start_date
    while current <= end_date:
        date_list.append(current)
        current += timedelta(days=1)

    return render(request, 'attendance_list.html', {
        'employees': employees,
        'records': records,
        'dates': date_list
    })
