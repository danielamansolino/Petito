from django.forms import ModelForm
from .models import Feeding, Cleaning, Loving, Moving, Sleeping

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['food']
    
class CleaningForm(ModelForm):
  class Meta:
    model = Cleaning
    fields = ['cleanup']
    

class LovingForm(ModelForm):
  class Meta:
    model = Loving
    fields = ['love']
    

class MovingForm(ModelForm):
  class Meta:
    model = Moving
    fields = ['move']
    

class SleepingForm(ModelForm):
  class Meta:
    model = Sleeping
    fields = ['sleep']
    