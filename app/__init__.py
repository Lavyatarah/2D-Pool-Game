from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv



#Initiliazing database, migration and JWT manager

db = SQLAlchemy()
Migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)


    #Loading environment variables from .env file
    load_dotenv()

    #Loading configuration from config.py
    app.config.from_object("config.config")

    #Initializing extemnsions with the app
    db.init_app(app)
    Migrate.init_app(app, db)
    jwt.init_app(app)