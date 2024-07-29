# Define a dictionary with meals and their ingredients
meals = {
    "tacos": ["cheese", "meat", "lettuce", "beans", "sour cream", "salsa", "guacamole"],
    "spaghetti": ["noodles", "meat", "sauce", "garlic bread"],
    "chicken curry": ["chicken", "curry powder", "coconut milk", "onions", "garlic", "ginger", "rice"],
    "salad": ["lettuce", "tomatoes", "cucumbers", "olive oil", "vinegar", "salt", "pepper"],
    "pizza": ["pizza dough", "tomato sauce", "cheese", "pepperoni", "bell peppers", "olives"],
    "pancakes": ["flour", "milk", "eggs", "syrup", "butter"],
    "stir fry": ["chicken", "broccoli", "carrots", "soy sauce", "garlic", "ginger", "rice"],
}

def generate_grocery_list(meal_names):
    grocery_list = []
    for meal in meal_names:
        if meal in meals:
            grocery_list.extend(meals[meal])
        else:
            print(f"Meal '{meal}' not found in the database.")
    
    # Remove duplicates and return the list
    return list(set(grocery_list))

def main():
    meal_names = []
    print("Enter the meals you want for the week. Type 'done' when you are finished." "\nNote: one meal per line")
    
    while True:
        meal = input("Enter a meal: ").lower()
        if meal == 'done':
            break
        meal_names.append(meal)
    
    grocery_list = generate_grocery_list(meal_names)
    print("\nYour grocery list:")
    for item in grocery_list:
        print(f"- {item}")

if __name__ == "__main__":
    main()
