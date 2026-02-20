from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
