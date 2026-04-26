
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_dashboard, name='home'),

    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/courses/', views.student_courses, name='student_courses'),
    path('student/notes/', views.student_notes, name='student_notes'),
    path('student/ai-tutor/', views.student_ai_tutor, name='student_ai_tutor'),
    path('teacher/courses/', views.teacher_courses),
    path('teacher/students/', views.teacher_students),
    path('teacher/ai-tutor/', views.teacher_ai_tutor),
    path('teacher/upload-note/', views.upload_note),
    path('teacher/add-quiz/', views.add_quiz),
    path('student/quiz/', views.student_quiz),
    
]
