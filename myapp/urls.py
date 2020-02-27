from django.urls import path
from myapp import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name="list"),
    path('create/', views.recipe_create, name="create"),
    path('<str:slug>/', views.recipe_details, name="details"),

]
