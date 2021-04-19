from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, UpdateView

from apps.todo.forms import RegisterTaskModelForm, AddCategoryForm
from apps.todo.models import Task, Category


class TaskList(ListView):
    model = Task
    paginate_by = 1


class TaskAList(ListView):
    model = Task
    paginate_by = 1
    template_name = 'todo/task_list.html'
    queryset = Task.objects.filter(priority='A')


class TaskBList(ListView):
    model = Task
    paginate_by = 1
    template_name = 'todo/task_list.html'
    queryset = Task.objects.filter(priority='B')


class TaskCList(ListView):
    model = Task
    paginate_by = 1
    template_name = 'todo/task_list.html'
    queryset = Task.objects.filter(priority='C')


class TaskListClassView(ListView):
    model = Task
    paginate_by = 1
    template_name = 'todo/task_list.html'
    queryset = Task.objects.past_tasks()


class CategoryList(ListView):
    model = Category
    paginate_by = 6


class TaskView(View):
    def get(self, request):
        form = RegisterTaskModelForm()
        return render(request, 'todo/add_task.html', {'form': form})

    def post(self, request):
        form = RegisterTaskModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            task_obj = Task(**validated_data)
            task_obj.save()
            return redirect('base')


class AddCategory(View):

    def get(self, request):
        form = AddCategoryForm()
        return render(request, 'todo/add_category.html', {"form": form})

    def post(self, request):
        note = ""
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            category_obj = Category(**validated_data)
            category_obj.save()
            note = 'Category added successfully '
        return render(request, 'todo/add_category.html', {'form': form, 'note': note})


class UpdateTask(UpdateView):
    model = Task
    template_name = 'todo/edit_task.html'
    fields = ['title', 'category', 'priority', 'content', 'time_to_do']
    success_url = '/tasks/'


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')


def task_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = True
    task.save()
    return redirect('task_list')
