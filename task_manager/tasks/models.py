from django.db import models

# Create your models here.

class Task(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT, related_name='statuses')
    author = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='authors')
    executor = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='executors', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

