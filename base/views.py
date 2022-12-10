from django.shortcuts import render, redirect
from .models import Todo


def home(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})


def add_todo(request):
    title = request.POST.get('title')
    Todo.objects.create(title=title)
    return redirect('home')


def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('home')


def edit_todo(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed')
        todo.title = title
        todo.completed = bool(completed)
        todo.save()
    
    return redirect('home')


def complete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.save()
    return redirect('home')
