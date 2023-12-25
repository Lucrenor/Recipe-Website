import app

class TestRecipe():
    def __init__():
        pass

    def Test_recipe():
        # Sample data for testing
        recipe_id = 1
        recipe_name = "Spaghetti Bolognese"
        dietary_needs = "None"
        cuisine = "Italian"
        meal_type = "Dinner"
        preparation_time = 30
        calorie = 500
        carbohydrates = 50
        protein = 20
        fat = 25
        instructions = "1. Boil water.\n2. Cook spaghetti.\n3. Prepare Bolognese sauce."
        ingredients = ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"]
        image_url = "https://example.com/spaghetti_bolognese.jpg"

        # Creating a recipe object
        recipe = app.Recipe(
            recipe_id, recipe_name, dietary_needs, cuisine, meal_type,
            preparation_time, calorie, carbohydrates, protein, fat,
            instructions, ingredients, image_url
        )

        # Check if all attributes are set correctly
        if (
            recipe.recipe_id == recipe_id and
            recipe.name == recipe_name and
            recipe.dietary_needs == dietary_needs and
            recipe.cuisine == cuisine and
            recipe.meal_type == meal_type and
            recipe.prep_time == preparation_time and
            recipe.calorie == calorie and
            recipe.carb == carbohydrates and
            recipe.protein == protein and
            recipe.fat == fat and
            recipe.instructions == instructions and
            recipe.ingredients == ingredients and
            recipe.image_url == image_url
        ):
            print("Test passed for Recipe.")
        
        else:
            print("Recipe Test Failed")


recipedatabase = app.RecipeDatabase()
class TestRecipeDatabase():
    def __init__():
        pass

    def TestAddandGetDB():
        conn, cursor = recipedatabase.connect_database()
        recipe_data = {
            'Recipe_name': 'Test Recipe',
            'Dietary_needs': 'Vegetarian',
            'Cuisine': 'Italian',
            'Meal_Type': 'Dinner',
            'Preparation_Time': 30,
            'Calorie': 500,
            'Carbohydrates': 50,
            'Protein': 20,
            'Fat': 10,
            'Instructions': 'Test instructions',
            'Ingredients': 'Test ingredients',
            'Imageurl': 'test_image.jpg'
        }
        app.recipe_db.add_recipe_to_database(recipe_data)

        # Check if the recipe is added by fetching details
        recipes = app.recipe_db.get_recipe_details()
        added_recipe = recipes[-1]  # Assuming the last recipe is the one just added
        recipeID = added_recipe['Recipe_ID']
        if all(added_recipe.get(key.lower()) == value for key, value in recipe_data.items()):
            print("Test passed for add and get recipe: All details match")
        else:
            print("Test Failed: Not all details match")
        delete_query = f"DELETE FROM recipes_final WHERE recipe_id = {recipeID};"
        cursor.execute(delete_query)
        conn.commit()

    
    def Test_get_cuisine_items():
    # Test fetching recipes by cuisine
        cuisine_name = 'Asian'
        Asian_recipes = app.recipe_db.get_cuisine_items(cuisine_name)
        if all(recipe['cuisine'] == cuisine_name for recipe in Asian_recipes):
            print("Test passed for get cuisine.")
        else:
            print("Test Failed for get cuisine.")

    def Test_get_popular():
        # Test fetching popular recipes
        popular_recipes = app.recipe_db.get_popular()
        # Check if at least one recipe is returned
        if popular_recipes:
            print("Test passed for get Popular Recipes.")
        else:
            print("Test Failed for get Popular Recipes.")

    def Test_get_veggie():
        # Test fetching vegetarian recipes
        veggie_recipes = app.recipe_db.get_veggie()
        if all(recipe['dietary_needs'] == 'Vegetarian' for recipe in veggie_recipes):
            print("Test passed for get Vegetarian Recipes.")
        else:
            print("Test Failed for get Vegetarian Recipes.")



recipe_db = app.RecipeDatabase()
info = app.Info(recipe_db)
conn, cursor = recipedatabase.connect_database()    

class TestInfo():
    def __init__():
        pass


    def Test_get_recipe_info():
        # Test getting recipe info by recipe_id
        recipe_data = {
            'Recipe_name': 'Test Recipe',
            'Dietary_needs': 'Vegetarian',
            'Cuisine': 'Italian',
            'Meal_Type': 'Dinner',
            'Preparation_Time': 30,
            'Calorie': 500,
            'Carbohydrates': 50,
            'Protein': 20,
            'Fat': 10,
            'Instructions': 'Test instructions',
            'Ingredients': 'Test ingredients',
            'Imageurl': 'test_image.jpg'
        }
        recipe_db.add_recipe_to_database(recipe_data)

        recipes = app.recipe_db.get_recipe_details()
        retrieved_recipe = recipes[-1]
        recipeID = retrieved_recipe['Recipe_ID']

        if all(retrieved_recipe.get(key.lower()) == value for key, value in recipe_data.items()):
            print("Test passed for get recipe info.")
        else:
            print("Test Failed: Not all details match")   
        delete_query = f"DELETE FROM recipes_final WHERE recipe_id = {recipeID};"
        cursor.execute(delete_query)
        conn.commit()


search_instance = app.Search(recipe_db)
class TestSearch():
    def Test_search():
        # Search for the added recipe
        search_term = 'Honey'
        search_results = search_instance.search(search_term)

        # Check if the search result contains the added recipe
        found_recipe = any(search_term in result[field]
        for result in search_results
        for field in ["Recipe_name", "Dietary_needs", "Cuisine", "Instructions", "Ingredients"])

        if found_recipe:
            print("Test passed for search.")    
        
        else:
            print("Test failed for search")

TestRecipe.Test_recipe()
TestRecipeDatabase.TestAddandGetDB()
TestRecipeDatabase.Test_get_cuisine_items()
TestRecipeDatabase.Test_get_popular()
TestRecipeDatabase.Test_get_veggie()
TestInfo.Test_get_recipe_info()
TestSearch.Test_search()
