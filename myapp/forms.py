from django import forms
from . import models


class CreateRecipe(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title', 'slug', 'body', 'thumb']


class EditArticle(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title', 'body', 'slug', 'thumb']