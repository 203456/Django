from django.db import models

# Importaciones de modelos
from django.contrib.auth.models import User



# Create your models here.
class Profiles(models.Model):
    id_user = models.OneToOneField(User, on_delete = models.CASCADE, null=False, blank=False)
    url_img = models.ImageField(null=True,blank=True, default='', upload_to='imgProfile/')


