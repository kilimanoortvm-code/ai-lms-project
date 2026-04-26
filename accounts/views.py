from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            role = form.cleaned_data.get('role')
            if role == 'teacher':
                user.is_teacher = True
            else:
                user.is_student = True

            user.save()
            login(request, user)

            if user.is_teacher:
                return redirect('/teacher/dashboard/')
            else:
                return redirect('/student/dashboard/')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            role = request.POST.get('role')

            if role == 'teacher' and user.is_teacher:
                return redirect('/teacher/dashboard/')
            elif role == 'student' and user.is_student:
                return redirect('/student/dashboard/')
            else:
                return redirect('/login/')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('/login/')
