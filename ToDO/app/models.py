from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    