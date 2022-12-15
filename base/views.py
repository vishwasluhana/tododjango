from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Todo


@login_required(login_url='login')
def home(request):
    todos = request.user.todo_set.all()
    user = request.user
    return render(request, 'index.html', {'todos': todos, 'user': user})


def add_todo(request):
    title = request.POST.get('title')
    Todo.objects.create(title=title, user=request.user)
    return redirect('home')


def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        todo.delete()
        return redirect('home')


def edit_todo(request, pk):
    todo = Todo.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed')
        todo.title = title
        todo.completed = bool(completed)
        todo.save()
    
    return redirect('home')


def complete_todo(request, pk):
    todo = Todo.objects.get(id=pk, user=request.user)
    todo.completed = True
    todo.save()
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        f = UserCreationForm()
    return render(request, 'register.html', {'form': f})
