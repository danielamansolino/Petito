from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') # later we need to RE-DIRECT to the INDEX!!!!
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def petitos_index(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'petitos/index.html', {
        'pets': pets 
    })

@login_required
def petitos_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'petitos/detail.html', {'pet':pet})


class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    fields = ['name', 'species', 'color', 'bio']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)