from django import forms
from .models import Student, Bill

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'full_name', 'course', 'year_level']


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['student', 'description', 'amount', 'due_date']
