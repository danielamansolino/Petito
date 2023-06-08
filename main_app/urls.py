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
    path('petitos/<int:pet_id>/tasks/', views.tasks, name='tasks'),
    path('petitos/<int:pet_id>/add_feeding/', views.add_feeding, name='feeding'),
    path('petitos/<int:pet_id>/add_cleaning/', views.add_cleaning, name='cleaning'),
    path('petitos/<int:pet_id>/add_loving/', views.add_loving, name='loving'),
    path('petitos/<int:pet_id>/add_moving/', views.add_moving, name='moving'),
    path('petitos/<int:pet_id>/add_sleeping/', views.add_sleeping, name='sleeping'),
    path('petitos/<int:pet_id>/task_feeding/', views.task_feeding, name='task_feeding'),
    path('petitos/<int:pet_id>/task_cleaning/', views.task_cleaning, name='task_cleaning'),
    path('petitos/<int:pet_id>/task_loving/', views.task_loving, name='task_loving'),
    path('petitos/<int:pet_id>/task_moving/', views.task_moving, name='task_moving'),
    path('petitos/<int:pet_id>/task_sleeping/', views.task_sleeping, name='task_sleeping'),
    path('petitos/<int:pet_id>/add_photo/', views.add_photo, name='add_photo'),

]