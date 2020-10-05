from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import TodoBoard
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form:
            form.save()
            messages.success(request, 'Todo added successfully')
            return redirect('todo:index')
    else:
        form = TodoForm()
        data = TodoBoard.objects.all()
        return render(request, 'index.html', {'form': form, 'data': data})


def edit(request, todo_id):
    if request.method == 'POST':
        item = TodoBoard.objects.get(pk=todo_id)
        form_data = TodoForm(request.POST, instance=item)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, f'Successfully updated {item.task}')
            return redirect('todo:index')
    else:
        item = TodoBoard.objects.get(pk=todo_id)
        return render(request, 'edit.html', {'item': item})


def delete(request, todo_id):
    if request.method == 'POST':
        item = TodoBoard.objects.get(pk=todo_id)
        item.delete()
        messages.success(request, f'Successfully updated {item.task}')
    return redirect('todo:index')
