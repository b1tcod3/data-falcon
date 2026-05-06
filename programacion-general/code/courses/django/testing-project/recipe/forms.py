from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la receta'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ingredientes (uno por línea)'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Instrucciones paso a paso'}),
        }
