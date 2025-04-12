from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    class Status(models.TextChoices):
        INPROGRESS = 'IP','InProgress'
        PENDING = 'PE','Pending'
        COMPLETED = 'CP','Completed'
    
    class Label(models.TextChoices):
        WORK = 'work', 'Work'
        GROCERY = 'grocery', 'Grocery'
        STUDY = 'study', 'Study'
        OTHER = 'other', 'Other'

    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User,related_name='my_tasks',on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING
    )
    label = models.CharField(
        max_length=20,
        choices=Label.choices,
        default=Label.OTHER
    )

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

