from django.db import models

# Create your models here.
class Pendaftaran(models.Model):
    nama = models.TextField()
    no_telepon = models.TextField(max_length=14)
