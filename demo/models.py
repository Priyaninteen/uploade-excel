from django.db import models

# Create your models here.
class UploadeFile(models.Model):
    file_path = models.FileField()
