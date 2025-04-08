from django.db import models
from django.utils import timezone  # Import timezone

class Consultation(models.Model):
    name        = models.CharField(max_length=255)
    contact     = models.CharField(max_length=255)
    email       = models.EmailField()
    date        = models.DateField(default=timezone.now)  # Provide default value
    comment     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation request by {self.name}"




