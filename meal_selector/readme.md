### Meal Selector App 
I've started working on a project to answer the ever-present "what should I cook?" question. This is currently in development, so consider this a rough draft!

## Current Version Notes
* Uses Pandas to read a .csv and convert to a dataframe
* Includes two functions:
    * `helper()`: Allows the user to specify paramaters for the meal they would like to eat. Function returns ALL meals that meet the given requirements. If you are in the mood for x, y, and z, this function will give you all of the possibilites. 
    * `chooser()`: Allows the user to specify paramaters for the meal they would like to eat. Returns a single random meal that meets the given requirements. This function is ideal if you do not want to make a decision, and want to be told what to cook. :)

## Tips for Using
* `meal_list`: Begin with a .csv of the meals you would like to include. 
    * I suggest creating the following columns: name, ingredients, type, effort. I also included the following columns, which may or may not be helpful for others: time, temperature, keywords, link.
    * For cells that have multiple values (like ingredients or keywords), use a semicolon (no space) instead of a comma to separate them.
    * Re: the inredient column: I plan to use this column simply to add items to my grocery list. As such, I did not include any ingredients that are regularly stocked in my pantry (spices, rice, olive oil, etc). The only exception is if the recipe uses a significant amount of something (for example, a whole stick of butter).
* Currently, all function inputs should be in the form of a dictionary. Include any parameters that you want your meal to meet.
    * For example, `{'type' : 'main', 'effort' : 'low'}` or `{'type' : 'breakfast', 'effort' : 'medium', 'temperature' : 'hot'}`

## What's Next?
* Re-design so that users can utilize a CLI to interact with the script (which will allow more user-friendly input methods, instead of a dictionary)
* Possible integration with Notion API, so that the ingredients list can be added to a shopping list
* Possible web scraper to pull recipes from a favorite site -> this would allow users to incorporate new recipes that they haven't tried yet