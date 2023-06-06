from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('petitos/', views.petitos_index, name='petitos'),
    path('petitos/<int:pet_id>/', views.petitos_detail, name='detail'),
    path('petitos/create/', views.PetCreate.as_view(), name='petitos_create'),
    path('petitos/<int:pk>/update/', views.PetUpdate.as_view(), name='petitos_update'),
    path('petitos/<int:pk>/delete/', views.PetDelete.as_view(), name='petitos_delete'), 
    path('petitos/<int:pet_id>/add_feeding/', views.add_feeding, name='feeding'),
    path('petitos/<int:pet_id>/tasks/', views.tasks, name='tasks'),

]