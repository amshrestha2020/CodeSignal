# You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

# Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

# Example

# For
#   dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
#             ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
#             ["Quesadilla", "Chicken", "Cheese", "Sauce"],
#             ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
# the output should be
#   solution(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
#                       ["Salad", "Salad", "Sandwich"],
#                       ["Sauce", "Pizza", "Quesadilla", "Salad"],
#                       ["Tomato", "Pizza", "Salad", "Sandwich"]]
# For
#   dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
#             ["Chicken Curry", "Chicken", "Curry Sauce"],
#             ["Fried Rice", "Rice", "Onions", "Nuts"],
#             ["Salad", "Spinach", "Nuts"],
#             ["Sandwich", "Cheese", "Bread"],
#             ["Quesadilla", "Chicken", "Cheese"]]
# the output should be
#   solution(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
#                       ["Chicken", "Chicken Curry", "Quesadilla"],
#                       ["Nuts", "Fried Rice", "Salad"],
#                       ["Onions", "Fried Rice", "Pasta"]]



def solution(dishes):
    # Create a dictionary to map ingredients to the list of dishes containing them
    ingredient_map = {}
    
    # Iterate through the dishes to populate the ingredient map
    for dish in dishes:
        dish_name = dish[0]
        ingredients = dish[1:]
        for ingredient in ingredients:
            if ingredient not in ingredient_map:
                ingredient_map[ingredient] = []
            ingredient_map[ingredient].append(dish_name)
    
    # Filter out ingredients with less than 2 dishes
    result = [[ingredient] + sorted(ingredient_map[ingredient]) for ingredient in ingredient_map if len(ingredient_map[ingredient]) >= 2]
    
    # Sort the result array lexicographically by ingredient names
    result.sort(key=lambda x: x[0])
    
    return result


