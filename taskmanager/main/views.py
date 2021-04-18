from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'main/delete.html'











