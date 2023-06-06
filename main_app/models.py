from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

SPECIES = (
    ('a', 'Unicorn'),
    ('b', 'Bear'),
    ('c', 'Cat'),
    ('d', 'Dinosaur')
)

COLORS = (
    ('1', 'Green'),
    ('2', 'Pink'),
    ('3', 'Purple'),
    ('4', 'Grey'),
    ('5', 'Yellow')
)

class Pet(models.Model):
    name =models.CharField(max_length=30)
    species = models.CharField (
        max_length=1,
        choices=SPECIES,
        default=SPECIES[0][0]
    )
    color = models.CharField (
        max_length=1,
        choices=COLORS,
        default=COLORS[0][0]
    )

    bio = models.TextField(max_length=1000)
    age = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id}) 
    
