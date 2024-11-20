import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "")


    #Database configuration

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("")

    #JWT Configuration

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")