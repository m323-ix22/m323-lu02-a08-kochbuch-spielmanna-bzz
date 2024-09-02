"""docstring for main.py"""

import json

def adjust_recipe(recipe, num_people):
    """Adjusts the recipe ingredients based on the number of people."""
    factor = num_people / recipe['servings']
    adjusted_ingredients = {ingredient: int(quantity * factor) for ingredient, quantity in recipe['ingredients'].items()}
    return {
        "title": recipe['title'],
        "ingredients": adjusted_ingredients,
        "servings": num_people
    }

def load_recipe(json_string):
    """Converts a JSON string into a Python dictionary representing a recipe."""
    return json.loads(json_string)

if __name__ == '__main__':
    # Example recipe JSON string
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    # Load the recipe
    recipe = load_recipe(recipe_json)

    # Adjust the recipe for 2 people
    adjusted_recipe = adjust_recipe(recipe, 2)

    # Print the adjusted recipe
    print(json.dumps(adjusted_recipe, indent=4))
