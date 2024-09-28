from django.shortcuts import render
from .forms import IngredientForm
from .huggingface_model import generate_recipe

def recipe_generator_view(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients'].split(",")           
            recipe = generate_recipe(ingredients)
            return render(request, 'suggestions.html', {'recipe': recipe, 'ingredients': ingredients})
    else:
        form = IngredientForm()
    return render(request, 'home.html', {'form': form})
