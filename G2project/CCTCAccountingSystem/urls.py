from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('show-students/', views.show_students, name='show_students'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),

    path('add-bill/', views.add_bill, name='add_bill'),
    path('show-bills/', views.show_bills, name='show_bills'),
    path('delete-bill/<int:bill_id>/', views.delete_bill, name='delete_bill'),
]
