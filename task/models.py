from django.db import models
from accounts.models import User


# Create your models here.
class TaskModel(models.Model):
    general_task = models.CharField(max_length=500, blank=False)
    project_management = models.CharField(max_length=500, blank=True)
    quality_analyst = models.CharField(max_length=500, blank=True)
    ui_or_ux = models.CharField(max_length=500, blank=True)
    meeting = models.CharField(max_length=500, blank=True)
    development = models.CharField(max_length=500, blank=True)
    blockers = models.BooleanField(default=False)
    comments = models.CharField(max_length=500, blank=True)
    time_off = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']


class MeetingModel(models.Model):
    description = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now=True)


class BlockersModel(models.Model):
    description = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now=True)

