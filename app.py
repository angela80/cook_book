import os
import os
from flask import Flask, render_template, redirect, request, url_for
#from flask_pymongo import PyMongo
#from bson.objectid import ObjectId



app = Flask(__name__)
#app.config["MONGO_DBNAME"] = 'healthy_recipe_manager'
#app.config["MONGO_URI"] = "mongodb://admin:gaslight318@ds055865.mlab.com:55865/healthy_recipe_manager"
#mongo = PyMongo(app)                







@app.route('/')
def hello():
    return 'Hello World ...again'







if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)