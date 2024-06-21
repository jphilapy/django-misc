from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/images', null=True)
    url = models.URLField(blank=True)
    slug = models.SlugField(unique=True, db_index=True, null=True)