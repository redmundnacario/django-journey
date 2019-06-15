from django.db import models

class command(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text