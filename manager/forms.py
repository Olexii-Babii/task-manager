from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from manager.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + ("position", )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ("first_name", "last_name", "email", "position",)


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    class Meta:
        model = Task
        fields = "__all__"


class TaskSearchForm(forms.Form):
    parameter = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Search by name, type"
            }
        )
    )
