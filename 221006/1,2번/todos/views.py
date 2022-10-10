from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse







# Create your views here.
def index(request):
    todos = Todo.objects.order_by('-pk')
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # 추가
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            # article = form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)


@require_POST
def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    todo = get_object_or_404(Todo, pk=pk)

    if todo.author == request.user:
        todo.delete()

    return redirect('todos:index')

@require_POST
def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed == 0:
        todo.completed = 1
        todo.save()
    else :
        todo.completed = 0
        todo.save()
    return redirect('todos:index')

