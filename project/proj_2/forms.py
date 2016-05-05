from django import forms


class TaskForm(forms.Form):
    task_code = forms.CharField(label='Kod czynności', max_length=20, required=1)
    wage = forms.FloatField(label='Stawka', max_value=999, min_value=0, required=1)
    id = forms.CharField(widget=forms.HiddenInput(), required=0)
    # id = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
