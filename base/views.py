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
    return render(request, 'delete.html', {'obj': todo})


def edit_todo(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        todo.title = title
        todo.save()
        return redirect('home')
    return render(request, 'edit.html', {'obj': todo})
