from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Course, Note, QuizQuestion
@login_required
def teacher_dashboard(request):
    courses = Course.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        Course.objects.create(title=title, description=description)
        return redirect('/teacher/dashboard/')

    return render(request, 'educator_portal/dashboard.html', {'courses': courses})


@login_required

def student_dashboard(request):
    courses = Course.objects.all()
    notes = Note.objects.all()

    return render(request, 'student/dashboard.html', {
        'courses': courses,
        'notes': notes
    })


@login_required
def student_courses(request):
    courses = Course.objects.all()
    return render(request, 'student/courses.html', {'courses': courses})

@login_required
def student_notes(request):
    return render(request, 'student/notes.html')

@login_required
def student_ai_tutor(request):
    return render(request, 'student/ai_tutor.html')
@login_required
def teacher_courses(request):
    courses = Course.objects.all()
    return render(request, 'educator_portal/courses.html', {'courses': courses})

@login_required
def teacher_students(request):
    return render(request, 'educator_portal/students.html')

@login_required
def teacher_ai_tutor(request):
    return render(request, 'educator_portal/ai_tutor.html')
from .models import Course, Note

@login_required
def upload_note(request):
    courses = Course.objects.all()

    if request.method == "POST":
        course_id = request.POST.get('course')
        title = request.POST.get('title')
        file = request.FILES.get('file')

        course = Course.objects.get(id=course_id)

        Note.objects.create(course=course, title=title, file=file)
        return redirect('/teacher/dashboard/')

    return render(request, 'educator_portal/upload_note.html', {'courses': courses})
@login_required
def add_quiz(request):
    courses = Course.objects.all()

    if request.method == "POST":
        course_id = request.POST.get('course')
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct_option = request.POST.get('correct_option')

        course = Course.objects.get(id=course_id)

        QuizQuestion.objects.create(
            course=course,
            question=question,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_option=correct_option
        )

        return redirect('/teacher/add-quiz/')

    return render(request, 'educator_portal/add_quiz.html', {'courses': courses})


@login_required
def student_quiz(request):
    questions = QuizQuestion.objects.all()

    if request.method == "POST":
        score = 0
        total = questions.count()

        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected == question.correct_option:
                score += 1

        return render(request, 'student/quiz_result.html', {
            'score': score,
            'total': total
        })

    return render(request, 'student/quiz.html', {'questions': questions})
