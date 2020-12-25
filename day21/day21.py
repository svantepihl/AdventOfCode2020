'''
--- Day 21: Allergen Assessment ---

You reach the train's last stop and the closest you can get to your vacation island without getting wet. 
There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. 
You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), 
the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, 
the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?
'''

def parse_input(path):
    ingredients_list = []
    file = open(path)
    for line in file.readlines():
        raw_ingredients,raw_allergens = line.strip().split('(')
        ingredients = set(raw_ingredients.strip().split())
        allergens = raw_allergens.rstrip(')').replace('contains ','').split(', ')
        ingredients_list.append([allergens,ingredients])
    return ingredients_list
 



def part_1(allergens_ingredients):
    all_possibilities = dict()
    safe_ingredients = set()

    # Create dict with all possible ingredients for each allergen
    for line in allergens_ingredients:
        allergens, ingredients = line

        for ingredient in ingredients:
            safe_ingredients.add(ingredient)

        for allergen in allergens:
            if not allergen in all_possibilities:
                all_possibilities[allergen] = [ingredients]
            else: 
                all_possibilities[allergen].append(ingredients)
    print(len(safe_ingredients))
    
    # For each allergen, select only ingredients that exsists in all sets
    all_allergens = dict()
    for allergen in all_possibilities: 
        all_allergens[allergen] = all_possibilities[allergen][0].intersection(*all_possibilities[allergen][1:])

    
    while any([len(all_allergens[allergen]) != 1 for allergen in all_allergens]):
        for allergen,ingredients in all_allergens.items():
            if len(ingredients) == 1:
                ingredient_to_remove = list(ingredients)[0]
                if ingredient_to_remove in safe_ingredients:
                    safe_ingredients.remove(ingredient_to_remove)
                    print(len(safe_ingredients))
                for other_allergen,other_ingredients in all_allergens.items():
                    if not other_allergen == allergen and ingredient_to_remove in other_ingredients:
                        all_allergens[other_allergen].remove(ingredient_to_remove)
    count = 0
    for allergen,ingredients in allergens_ingredients:
        occurences = len(safe_ingredients.intersection(set(ingredients)))
        count += occurences
    return count,all_allergens

inp = parse_input('day21/input.txt')
part_1,all_allergens = (part_1(inp))

'''
--- Part Two ---

Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.
Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
'''
part_2 = list(all_allergens.items())
part_2.sort()
result = ''
for allergen,ingredient in part_2:
   result += list(ingredient)[0] + ','

print(result.rstrip(',')) 
