from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import os 

load_dotenv()

app = Flask(
    __name__,
    static_url_path='', 
    static_folder='static'
)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+ os.getenv("DB_USERNAME") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv("DB_HOST") + "/" + os.getenv("DB_DATABASE")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)