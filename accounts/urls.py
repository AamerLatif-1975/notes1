from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('edit-staff/<int:pk>/', views.edit_staff, name='edit_staff'),
    path('staff/delete/<int:pk>/', views.delete_staff, name='delete_staff'),
]
