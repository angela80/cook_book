import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config["MONGO_DBNAME"] ='healthy_recipe_manager'
app.config["MONGO_URI"] = "mongodb://root:gaslight318@ds055865.mlab.com:55865/healthy_recipe_manager"
mongo = PyMongo(app)                


@app.route('/Home', methods = ["GET","POST"])
def Homepage():
    return('Homepage.html')
#    recipe=mongo.db.recipes.find()
  #  return render_template('home.html')
    


@app.route('/')
@app.route('/get_recipes')
def Recipes():
    return render_template("Recipes.html",
    recipes=mongo.db.recipes.find())



@app.route('/Add_Recipe')
def Add_Recipe():
    return render_template('Add_Recipe.html')



@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)