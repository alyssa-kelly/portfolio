import random
import pandas as pd
df = pd.read_csv ('/Users/alyssa/Documents/portfolio/adhd_menu/meal_list.csv', index_col=None)
meal_list = df.to_dict(orient='records')
      
def helper(param): # param is a dict with any requirements ex: {'type' : 'main', 'effort' : 'low'}
    results = []
    for each in meal_list:
        reqts = []
        for k, v in param.items():
            if (k, v) in each.items():
                reqts.append('met')
            else:
                reqts.append('unmet')
        if 'unmet' not in reqts:
            results.append(each['name'])
    return results
        
def chooser(param):
    return random.choice(helper(param))

# print(chooser({'type' : 'main', 'effort' : 'low'}))
print(helper({'type' : 'main', 'temperature' : 'hot', 'effort' : 'medium'}))
