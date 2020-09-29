from django.urls import path
from student import views

urlpatterns = [
    path('school/', views.SchoolView.as_view(), name='schools'),
    path('school/<int:school_id>/', views.SchoolDetailView.as_view(), name='school-detail'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('student/<int:student_id>/', views.StudentDetailView.as_view(), name='student')
    ]

