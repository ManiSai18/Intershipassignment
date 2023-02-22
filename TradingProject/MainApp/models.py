from django.db import models

# Create your models here.
class Trading(models.Model):
    csvfile = models.FileField(upload_to='files')