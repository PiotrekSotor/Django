from django.db import models
import datetime

# Create your models here.

class Task(models.Model):
    task_code = models.CharField(max_length=200, unique=1)
    wage = models.FloatField(default=0)
    
    def __str__(self):
        return "%s - %s" % (self.task_code, self.wage)
    
class Worker(models.Model):
    name = models.CharField(max_length=200, unique=1)
    
    def __str__(self):
        return self.name
    
class Job(models.Model):
    task_code = models.ForeignKey(Task, on_delete=models.CASCADE)
    person = models.ForeignKey(Worker, on_delete=models.CASCADE)
    count = models.FloatField(default=0)
    date = models.DateTimeField('date published', )
    
    def __str__(self):
        return "%s - %s - %s - %s" % (self.date, self.task_code, self.person, self.count)
