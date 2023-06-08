from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from datetime import date 

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

FEED = (
    ('food1', 'feed burger'),
    ('food2', 'feed kale soup'),
    ('food3', 'feed donut'),
)

CLEAN = (
    ('clean1', 'clean poop'),
    ('clean2', 'bathe'),
)

LOVE = (
    ('love1', 'give a hug'),
    ('love2', 'give kisses'),
)

MOVE = (
    ('move1', 'play fetch'),
    ('move2', 'go for a walk'),
)

SLEEP = (
    ('sleep1', 'take a nap'),
)

class Pet(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(
        max_length=1,
        choices=SPECIES,
        default=SPECIES[0][0]
    )
    color = models.CharField(
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
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(FEED)
    
    def clean_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count() >= len(CLEAN)
    
    def love_for_today(self):
        return self.loving_set.filter(date=date.today()).count() >= len(LOVE)
    
    def play_for_today(self):
        return self.moving_set.filter(date=date.today()).count() >= len(MOVE)
    
    def sleep_for_today(self):
        return self.sleeping_set.filter(date=date.today()).count() >= len(SLEEP)
    


class Feeding(models.Model):
    date = models.DateField(auto_now_add=True)
    food = models.CharField(
        max_length=6,
        choices=FEED,
        default=FEED[0][0]
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.food}'


class Cleaning(models.Model):
    date = models.DateField(auto_now_add=True)
    cleanup = models.CharField(
        max_length=6,
        choices=CLEAN,
        default=CLEAN[0][0]
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.cleanup}'

class Loving(models.Model):
    date = models.DateField(auto_now_add=True)
    love = models.CharField(
        max_length=6,
        choices=LOVE,
        default=LOVE[0][0]
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.love}'
    

class Moving(models.Model):
    date = models.DateField(auto_now_add=True)
    move = models.CharField(
        max_length=6,
        choices=MOVE,
        default=MOVE[0][0]
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.move}'
    

class Sleeping(models.Model):
    date = models.DateField(auto_now_add=True)
    sleep = models.CharField(
        max_length=6,
        choices=SLEEP,
        default=SLEEP[0][0]
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.sleep}'
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"  