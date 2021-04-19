from django.urls import path
from django.views.generic import TemplateView

from apps.todo import views
from apps.todo.views import TaskView, TaskListClassView, AddCategory, UpdateTask, task_delete, task_done, \
    category_delete, TaskAList, TaskBList, \
    TaskCList

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('taskpriority', TemplateView.as_view(template_name='todo/tasks-priority.html'), name='task-priority'),
    path('category_list/', views.CategoryList.as_view(), name='category_list'),
    path('add_task/', TaskView.as_view(), name="task"),
    path('add_category/', AddCategory.as_view(), name="add_category"),
    path('past_task/', TaskListClassView.as_view(), name="past_task"),
    path('edit_task/<int:pk>', UpdateTask.as_view(), name="edit_task"),
    path('task_delete/<int:pk>', task_delete, name="task_delete"),
    path('category_delete/<int:pk>', category_delete, name="category_delete"),
    path('task_done/<int:pk>', task_done, name="task_done"),
    path('task_a/', TaskAList.as_view(), name="task_a"),
    path('task_b/', TaskBList.as_view(), name="task_b"),
    path('task_c/', TaskCList.as_view(), name="task_c"),

]
