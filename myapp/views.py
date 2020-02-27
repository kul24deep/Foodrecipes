from django.shortcuts import render, redirect
from django.http import HttpResponse
from scipy.constants import slug

from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.


def recipes(request):
    recipe = Recipe.objects.all().order_by('date')
    return render(request, 'myapp/recipes.html', {'recipes': recipe})


def recipe_details(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'myapp/recipe_detail.html', {'recipe': recipe})


@login_required(login_url="/accounts/login/")
def recipe_create(request):
    if request.method == 'POST':
        form = forms.CreateRecipe(request.POST, request.FILES)
        if form.is_valid():
            # save recipe to db
            instance = form.save(commit=False)
            instance.writer = request.user
            instance.save()
            return redirect('recipes:list')
    else:
        form = forms.CreateRecipe()
    return render(request, 'myapp/create.html', {'form': form})


def edit_article(request):
    return render(request, 'myapp/edit_article.html')
