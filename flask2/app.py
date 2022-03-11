# Example 1
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# Example 2
from main import db,app
from models import User,Product
from seeders import RunSeeder
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
import sys

Migrate(app, db)
FlaskSeeder(app,db)

if len(sys.argv) == 3:
    if sys.argv[1] == "seed" and sys.argv[2] == "run":
        RunSeeder(db,user=User,product=Product)
else:
    import views
    
    @app.route("/")
    def index():
        return "Oke"
        
    if __name__ == "__main__":
        app.run()