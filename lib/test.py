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

# def print_spicy_foods(spicy_foods):
#     spiciest_foods = [food for food in spicy_foods if food["heat_level"]> 5]
#     for food in spiciest_foods:
#         heat_emoji = "🌶"* food["heat_level"]
#         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")
        
# print_spicy_foods(spicy_foods)

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             print(food) 
#     print(None) 
    
# get_spicy_food_by_cuisine(spicy_foods, 'American')  

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    number_of_foods = len(spicy_foods)
    print(total_heat // number_of_foods)
 
get_average_heat_level(spicy_foods)