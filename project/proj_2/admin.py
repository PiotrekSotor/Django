from django.contrib import admin

from .models import Worker, Job, Task
admin.site.register(Worker)
admin.site.register(Job)
admin.site.register(Task)