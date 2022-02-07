from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class imgField(models.Model):
    name_img = models.CharField(max_length=10, null = False)
    url_img = models.ImageField(max_length=100, null = False, default='', upload_to='assets/img/')
    format_img = models.CharField(max_length=100, null = False)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

