#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    """
    recipe_keys = recipe.keys()
    ingredients_keys = ingredients.keys()
    if recipe_keys != ingredients_keys:
        return 0

    count = 0
    have_enough = True
    while have_enough == True:
        for key in recipe:
            ingredients[key] -= recipe[key]
            if ingredients[key] < 0:
                have_enough = False
                break
                
        if have_enough == True: count += 1

    return count
    """
    recipe_keys = recipe.keys()
    ingredients_keys = ingredients.keys()
    if recipe_keys != ingredients_keys:
        return 0

    totals = {}
    for key in recipe:
        totals[key] = ingredients[key] / recipe[key]
    
    least = None 
    for key in totals:
        if least is None or (totals[key] > 1 and totals[key] < least):
            least = totals[key]

    return round(least)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
