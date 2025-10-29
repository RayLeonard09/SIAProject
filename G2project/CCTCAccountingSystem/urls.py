from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('add-entry/', views.add_entry, name='add_entry'),  # replaces add-bill
    path('edit-entry/', views.edit_entry, name='edit_entry'),
    path('edit-bill/<int:bill_id>/', views.edit_bill, name='edit_bill'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('delete-bill/<int:bill_id>/', views.delete_bill, name='delete_bill'),
    path('records/', views.records, name='records'),
]
