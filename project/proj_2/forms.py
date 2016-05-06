from django import forms
from .models import Task, Worker
from datetime import date

class TaskForm(forms.Form):
    task_code = forms.CharField(label='Kod czynności', max_length=20, required=1)
    wage = forms.FloatField(label='Stawka', max_value=999, min_value=0, required=1)
    id = forms.CharField(widget=forms.HiddenInput(), required=0)
    # id = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WorkerForm(forms.Form):
    name = forms.CharField(label='Nazwa pracownika', max_length=50, required=1)
    id = forms.CharField(widget=forms.HiddenInput(), required=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class JobForm(forms.Form):
    task_code_field = forms.CharField(label='Kod czynności', max_length=20, required=0)
    task_code_combobox = forms.ModelChoiceField(queryset=Task.objects.order_by('task_code'), required=0)
    worker_field = forms.CharField(label='Pracownik', max_length=50, required=0)
    worker_combobox = forms.ModelChoiceField(queryset=Worker.objects.order_by('name'), required=0)
    date = forms.DateField(required=0)
    count = forms.FloatField(label='Ilość', min_value=0, max_value=99999, required=0)

    id = forms.CharField(widget=forms.HiddenInput(), required=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AggregatorForm(forms.Form):
    startdate = forms.DateField(required=1)
    enddate = forms.DateField(required=1)
    workers = forms.ModelMultipleChoiceField(queryset=Worker.objects.order_by('name'), required=1)
    tasks = forms.ModelMultipleChoiceField(queryset=Task.objects.order_by('task_code'),required=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)