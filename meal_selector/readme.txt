to use the adhd menu:

meal_list should be saved as a csv file with the following columns
    - required: name, ingredients, type, effort
    - optional: time, temperature, keywords, link

for cells that have multiple values (like ingredients or keywords), use a semicolon (no space) instead of a comma to separate them
re: ingredient
    - do what makes sense for you. you can include the full list with measurements if that is helpful.
    - i plan to only use this to select meals and figure out what to put on my grocery list
    - as such, i did not include any ingredients that we regularly stock in our pantry (spices, rice, olive oil, etc)
    - the only exception is if the recipe using a significant amount of something (for example, a whole stick of butter)

both helper and chooser functions take a dictionary as an argument (example: {'type' : 'main', 'effort' : 'low'})

the helper function will return ALL meals that match the parameters given (example: all medium effort breakfasts)
the chooser function will select and return a random meal that meets the parameters given