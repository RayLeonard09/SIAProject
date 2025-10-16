from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Bill

# --- Home Page ---
def home(request):
    return render(request, 'invApp/home.html')


# --- ADD STUDENT ---
def add_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        full_name = request.POST.get('name')
        course = request.POST.get('course')
        year_level = request.POST.get('year_level')

        # Basic validation
        if student_id and full_name and course and year_level:
            Student.objects.create(
                student_id=student_id,
                full_name=full_name,
                course=course,
                year_level=year_level
            )
            return redirect('show_students')

    return render(request, 'invApp/add_student.html')


# --- SHOW STUDENTS ---
def show_students(request):
    students = Student.objects.all()
    return render(request, 'invApp/show_student.html', {'students': students})


# --- DELETE STUDENT ---
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('show_students')


# --- ADD BILL ---
def add_bill(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        due_date = request.POST.get('due_date')

        student = get_object_or_404(Student, student_id=student_id)
        Bill.objects.create(
            student=student,
            description=description,
            amount=amount,
            due_date=due_date
        )
        return redirect('show_bills')

    students = Student.objects.all()
    return render(request, 'invApp/add_bill.html', {'students': students})


# --- SHOW BILLS ---
def show_bills(request):
    bills = Bill.objects.select_related('student').all()
    return render(request, 'invApp/show_bill.html', {'bills': bills})


# --- DELETE BILL ---
def delete_bill(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    bill.delete()
    return redirect('show_bills')
