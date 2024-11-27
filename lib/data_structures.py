spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_name = [food["name"] for food in spicy_foods]
    return food_name
    
def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"]> 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"]]
    for food in spiciest_foods:
        heat_emoji = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"]== cuisine:
            return food

def print_spiciest_foods(spicy_foods):
   spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
   for food in spiciest_foods:
        heat_emoji = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")

def get_average_heat_level(spicy_foods):
    sum_of_heat_levels = sum(food['heat_level'] for food in spicy_foods)
    foods_count = len(spicy_foods)
    return (sum_of_heat_levels// foods_count)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
