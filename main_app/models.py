from django.db import models
from django.contrib.auth.models import User

# Create your models here.

IMAGES = (
    ('A', 'Pet A'),
    ('B', 'Pet B'),
    ('C', 'Pet C'),
    ('D', 'Pet D')
)

class Pet(models.Model):
    name =models.CharField(max_length=30)
    image = models.CharField (
        max_length=1,
        choices=IMAGES,
        default=IMAGES[0][0]
    )
    bio = models.TextField(max_length=1000)
    age = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
