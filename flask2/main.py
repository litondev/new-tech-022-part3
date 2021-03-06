from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import logging
from flask_cors import CORS
import os 

load_dotenv()

app = Flask(
    __name__,
    static_url_path='', 
    static_folder='static'
)

CORS(app)

logging.basicConfig(
    filename='logging.log', 
    level=logging.WARNING, 
    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+ os.getenv("DB_USERNAME") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv("DB_HOST") + "/" + os.getenv("DB_DATABASE")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'

db = SQLAlchemy(app)