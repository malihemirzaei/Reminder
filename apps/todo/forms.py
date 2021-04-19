from django import forms

from apps.todo.models import Task, Category


class RegisterTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'priority', 'content', 'time_to_do', ]


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
