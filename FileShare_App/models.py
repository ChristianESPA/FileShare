from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UploadFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
