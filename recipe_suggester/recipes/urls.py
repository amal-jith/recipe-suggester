from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_generator_view, name='home'),

]