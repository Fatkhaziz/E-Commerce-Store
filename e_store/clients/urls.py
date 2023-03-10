from django.urls import path
from . import views
from django.views.generic.edit import CreateView


urlpatterns = [
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('update', views.update_profile, name='update')
]