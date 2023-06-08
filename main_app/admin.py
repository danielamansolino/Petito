from django.contrib import admin
from .models import Pet, Feeding, Cleaning, Loving, Moving, Sleeping, Photo

# Register your models here.

admin.site.register(Pet)
admin.site.register(Feeding)
admin.site.register(Cleaning)
admin.site.register(Loving)
admin.site.register(Moving)
admin.site.register(Sleeping)
admin.site.register(Photo)