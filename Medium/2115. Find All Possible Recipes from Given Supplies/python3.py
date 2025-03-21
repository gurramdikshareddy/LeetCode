from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Initialize a set of supplies for quick lookup
        supply_set = set(supplies)
        result = []

        # Map each recipe to its list of ingredients
        recipe_to_ingredients = {recipes[i]: set(ingredients[i]) for i in range(len(recipes))}

        # We will continue the process until no new recipes can be created
        while True:
            new_recipe_found = False

            # Try to create each recipe if its ingredients are available in supply_set
            for recipe in recipes:
                if recipe in supply_set:
                    continue  # Skip already creatable recipes

                # Check if all ingredients for the recipe are available in supply_set
                if all(ingredient in supply_set for ingredient in recipe_to_ingredients[recipe]):
                    supply_set.add(recipe)  # Now we can create this recipe, add it to supplies
                    result.append(recipe)  # Add to the result list
                    new_recipe_found = True

            # If no new recipe was found, we can stop
            if not new_recipe_found:
                break

        return result
