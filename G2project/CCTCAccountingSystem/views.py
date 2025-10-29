from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student, Bill


# --- HOME PAGE ---
def home(request):
    return render(request, 'invApp/home.html')


# --- ADD STUDENT OR BILL ---
@login_required(login_url="/login/")
def add_entry(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Add Student
        if form_type == 'student':
            student_id = request.POST.get('student_id')
            full_name = request.POST.get('name')
            course = request.POST.get('course')
            year_level = request.POST.get('year_level')

            if student_id and full_name and course and year_level:
                Student.objects.create(
                    student_id=student_id,
                    full_name=full_name,
                    course=course,
                    year_level=year_level
                )

        # Add Bill
        elif form_type == 'bill':
            student_id = request.POST.get('student_id')
            description = request.POST.get('description')
            amount = request.POST.get('amount')
            due_date = request.POST.get('due_date')

            if student_id and description and amount and due_date:
                student = get_object_or_404(Student, student_id=student_id)
                Bill.objects.create(
                    student=student,
                    description=description,
                    amount=amount,
                    due_date=due_date
                )

        return redirect('records')

    students = Student.objects.all()
    return render(request, 'invApp/records.html', {'students': students})


# --- EDIT STUDENT OR BILL ---
@login_required(login_url="/login/")
def edit_entry(request):
    if request.method == "POST":
        entry_type = request.POST.get("entry_type")
        entry_id = request.POST.get("entry_id")

        if entry_type == "bill":
            bill = get_object_or_404(Bill, id=entry_id)
            bill.description = request.POST.get("description")
            bill.amount = request.POST.get("amount")
            bill.due_date = request.POST.get("due_date")
            bill.save()

        elif entry_type == "student":
            student = get_object_or_404(Student, id=entry_id)
            student.student_id = request.POST.get("student_id")
            student.full_name = request.POST.get("name")
            student.course = request.POST.get("course")
            student.year_level = request.POST.get("year_level")
            student.save()

    return redirect("records")


# --- EDIT BILL (INDIVIDUAL) ---
@login_required(login_url="/login/")
def edit_bill(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    if request.method == "POST":
        bill.description = request.POST.get("description")
        bill.amount = request.POST.get("amount")
        bill.due_date = request.POST.get("due_date")
        bill.save()
        return redirect("records")
    return render(request, 'invApp/edit_bill.html', {'bill': bill})


# --- SHOW RECORDS (VISIBLE TO EVERYONE) ---
def records(request):
    bills = Bill.objects.select_related('student').all()
    students = Student.objects.all()
    return render(request, 'invApp/records.html', {
        'bills': bills,
        'students': students
    })


# --- DELETE STUDENT ---
@login_required(login_url="/login/")
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('records')


# --- DELETE BILL ---
@login_required(login_url="/login/")
def delete_bill(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    bill.delete()
    return redirect('records')


# --- ADMIN LOGIN / LOGOUT ---
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('records')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('admin_login')

    return render(request, 'invApp/admin_login.html')


def admin_logout(request):
    logout(request)
    return redirect('records')
