from flask import Flask, request, render_template, jsonify
import psycopg2
from flask_cors import CORS


class Recipe:
    def __init__(self, name, dietary_needs, meal_type, prep_time, calorie, carb, protein, fat, instructions, ingredients):
        self.name = name
        self.dietary_needs = dietary_needs
        self.meal_type = meal_type
        self.prep_time = prep_time
        self.calorie = calorie
        self.carb = carb
        self.protein = protein
        self.fat = fat
        self.instructions = instructions
        self.ingredients = ingredients

class RecipeDatabase():
    def __init__(self):
        self.conn, self.cursor = self.connect_database()


    def connect_database(self):
        conn = psycopg2.connect(
                host = "localhost",
                dbname = "recipe",
                user = "postgres",
                password = "eren",
                port = 5432
        )
        conn.autocommit = True
        cursor = conn.cursor()
        return conn, cursor

    def add_recipe_to_database(self, recipe):
        pass


    def get_recipe_details(self):
        recipe_data = "SELECT * FROM recipes ORDER BY recipe_id;"
        cursor.execute(recipe_data)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description][1:]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageUrl"] = row[-1]
            result.append(d_data)
        return result
     
    def get_cuisine_items(self, cuisine_name):
        self.cuisine_name = cuisine_name
        cuisine_to_search = cuisine_name
        cuisine_data = f"SELECT * FROM recipes WHERE Cuisine = '{cuisine_to_search}' ORDER BY recipe_id;"
        cursor.execute(cuisine_data)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description][1:3]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageUrl"] = row[-1]
            result.append(d_data)
        return result
    






class Info():
    def __init__(self, recipe_db):
        self.recipe_db = recipe_db
    
    def get_recipe_info(self, recipe_id):
        self.cuisine_name = recipe_id
        recipe_to_search = recipe_id
        cuisine_data = f"SELECT * FROM recipes WHERE recipe_id = '{recipe_to_search}' ORDER BY recipe_id;"
        cursor.execute(cuisine_data)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description][1:]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageUrl"] = row[-1]
            result.append(d_data)
        print(result)
        return result
      

class Search:
    def __init__(self, recipe_db):
        self.recipe_db = recipe_db

    def search(self, search_term):
        self.search_term = search_term
        recipe_data = """
            SELECT * 
            FROM recipes 
            WHERE 
                recipe_name ILIKE %(search_term)s OR
                Dietary_needs ILIKE %(search_term)s OR
                Cuisine ILIKE %(search_term)s OR
                Instructions ILIKE %(search_term)s OR
                Ingredients ILIKE %(search_term)s 
            ORDER BY recipe_id;
        """
        cursor.execute(recipe_data, {'search_term': '%' + search_term + '%'})
        rows = cursor.fetchall()

        # Sonuçları JSON formatında döndürün
        result = [{'Recipe_ID': row[0], 'Recipe_name': row[1], "imageUrl":row[12]} for row in rows]
        return result



app = Flask(__name__)
CORS(app)


recipe_db = RecipeDatabase()
info_handler = Info(recipe_db)
search_handler = Search(recipe_db)



@app.route('/api/get_cuisine', methods=['POST'])
def APİ_get_cuisine_recipes():
    request_data = request.get_json() 
    #Buradaki name İtalian vs vs.
    name = request_data.get("name")
    cuisine_data = recipe_db.get_cuisine_items(name)
    return jsonify(cuisine_data)


@app.route('/api/info', methods=['POST'])
def APİ_get_info():
    request_data = request.get_json() 
    #Buradaki name İtalian vs vs.
    name = request_data.get("name")
    ingredient_data = info_handler.get_recipe_info(name)
    return jsonify(ingredient_data)


@app.route('/api/search', methods=['POST'])
def APİ_search():
    request_data = request.get_json() 
    #Buradaki name İtalian vs vs.
    name = request_data.get("name")
    searched_data =search_handler.search(name)

    return jsonify(searched_data)


#Connect recipe database
conn, cursor = recipe_db.connect_database()

#Get recipe data
recipe_data = recipe_db.get_recipe_details()




if __name__ == '__main__':
    app.run(debug=True)


"""recipe extend recipedatabase
instruction , ingridients extend recipe """