def check_ingredient_match(recipe, inventory):
    matched_items = 0
    missing_ingredients = []
    for ingredient in recipe:
        if ingredient in inventory:
            matched_items += 1
        else:    
            missing_ingredients.append(ingredient)
    percentage = (matched_items/len(recipe)) * 100
    return percentage, missing_ingredients
