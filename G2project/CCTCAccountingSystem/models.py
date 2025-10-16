from django.db import models

class Student(models.Model):
    student_id = models.TextField(unique=True)
    full_name = models.TextField()
    course = models.TextField()
    year_level = models.TextField()

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"


class Bill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.description} - ₱{self.amount} ({self.student.full_name})"
