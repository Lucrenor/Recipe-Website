from flask import Flask, request, render_template, jsonify
import psycopg2
from flask_cors import CORS
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid

class Recipe:
    def __init__(self, Recipe_ID, recipe_name, dietary_needs,cuisine , meal_type, preparation_time, calorie, carbohydrates, protein, fat, instructions, ingredients, imageurl):
        self.recipe_id = Recipe_ID
        self.name = recipe_name
        self.dietary_needs = dietary_needs
        self.cuisine = cuisine
        self.meal_type = meal_type
        self.prep_time = preparation_time
        self.calorie = calorie
        self.carb = carbohydrates
        self.protein = protein
        self.fat = fat
        self.instructions = instructions
        self.ingredients = ingredients
        self.image_url = imageurl

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

    def add_recipe_to_database(self, recipe_data):
        self.cursor.execute('INSERT INTO recipes_final ('
                    'recipe_name, dietary_needs, cuisine, meal_type, '
                    'preparation_time, calorie, carbohydrates, protein, fat, '
                    'instructions, ingredients, imageurl) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (recipe_data['Recipe_name'], recipe_data['Dietary_needs'], recipe_data['Cuisine'],
                     recipe_data['Meal_Type'], recipe_data['Preparation_Time'], recipe_data['Calorie'],
                     recipe_data['Carbohydrates'], recipe_data['Protein'], recipe_data['Fat'],
                     recipe_data['Instructions'], recipe_data['Ingredients'], recipe_data['Imageurl']))

        self.conn.commit()



    def get_recipe_details(self):
        recipe_data = "SELECT * FROM recipes_final ORDER BY recipe_id;"
        cursor.execute(recipe_data)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description][1:]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageurl"] = row[-1]
            result.append(d_data)
        return result
     
    def get_cuisine_items(self, cuisine_name):
        self.cuisine_name = cuisine_name
        cuisine_to_search = cuisine_name
        cuisine_data = f"SELECT * FROM recipes_final WHERE Cuisine = '{cuisine_to_search}' ORDER BY recipe_id;"
        cursor.execute(cuisine_data)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description][1:5]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageurl"] = row[-1]
            result.append(d_data)
        return result
    
    def get_popular(self):
        recipe_data_query = "SELECT * FROM recipes_final ORDER BY recipe_id;"
        cursor.execute(recipe_data_query)
        rows = cursor.fetchmany(10)
        colnames = [desc[0] for desc in cursor.description][1:3]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageurl"] = row[-1]
            result.append(d_data)
        return result
    
    
        
    def get_veggie(self):
        recipe_data_query = "SELECT * FROM recipes_final WHERE dietary_needs = 'Vegetarian' ORDER BY recipe_id;"
        cursor.execute(recipe_data_query)

        rows = cursor.fetchmany(8)

        colnames = [desc[0] for desc in cursor.description][1:4]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageurl"] = row[-1]
            result.append(d_data)
        return result
    


class Info():
    def __init__(self, recipe_db):
        self.recipe_db = recipe_db
    
    def get_recipe_info(self, recipe_id):
        self.cuisine_name = recipe_id
        recipe_to_search = recipe_id
        cuisine_data = f"SELECT * FROM recipes_final WHERE recipe_id = '{recipe_to_search}' ORDER BY recipe_id;"
        cursor.execute(cuisine_data)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description][1:]
        result = []
        for row in rows:
            d_data = {"Recipe_ID": row[0]}
            for i in range(1, len(colnames)):
                d_data[colnames[i-1]] = row[i]
            d_data["imageurl"] = row[-1]
            result.append(d_data)
        return result
      

class Search:
    def __init__(self, recipe_db):
        self.recipe_db = recipe_db

    def search(self, search_term):
        self.search_term = search_term
        recipe_data = """
            SELECT * 
            FROM recipes_final 
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

        result = [{'Recipe_ID': row[0], 'Recipe_name': row[1], "Dietary_needs": row[2], "Cuisine":row[3], "Instructions": row[10],"Ingredients":row[11] , "imageurl":row[12]} for row in rows]
        return result



app = Flask(__name__)
CORS(app)

recipes= []
recipe_db = RecipeDatabase()
info_handler = Info(recipe_db)
search_handler = Search(recipe_db)



@app.route('/api/add_recipe', methods=['POST'])
def APİ_add_recipe():
    recipe_data = request.form.to_dict()

    if 'Imageurl' in request.files:
        img_file = request.files['Imageurl']
        filename = str(uuid.uuid4()) + '_' + secure_filename(img_file.filename)
        # Save the file to the 'public/img/save' folder
        save_path = os.path.join('public', 'img', filename)
        img_file.save(save_path)
        img_path = "/img/" + filename
        recipe_data['Imageurl'] = img_path
    
    recipe_db.add_recipe_to_database(recipe_data)
    return "Completed"

@app.route('/api/get_cuisine', methods=['POST'])
def APİ_get_cuisine_recipes():
    request_data = request.get_json() 
    name = request_data.get("name")
    cuisine_data = recipe_db.get_cuisine_items(name)
    return jsonify(cuisine_data)


@app.route('/api/info', methods=['POST'])
def APİ_get_info():
    request_data = request.get_json() 
    name = request_data.get("name")
    ingredient_data = info_handler.get_recipe_info(name)
    recipes = [Recipe(**data) for data in recipe_data]
    return jsonify(ingredient_data)


@app.route('/api/search', methods=['POST'])
def APİ_search():
    request_data = request.get_json() 
    name = request_data.get("name")
    searched_data =search_handler.search(name)

    return jsonify(searched_data)

@app.route('/api/veggie', methods=['POST'])
def APİ_veggie():
    result = recipe_db.get_veggie()
    return jsonify(result)

@app.route('/api/popular', methods=['POST'])
def APİ_popular():
    result = recipe_db.get_popular()
    return jsonify(result)

#Connect recipe database
conn, cursor = recipe_db.connect_database()

#Get recipe data
recipe_data = recipe_db.get_recipe_details()


if __name__ == '__main__':
    app.run(debug=True)
