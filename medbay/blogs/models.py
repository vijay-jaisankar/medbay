from django.db import models
from users.models import User, Doctor

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Doctor, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title