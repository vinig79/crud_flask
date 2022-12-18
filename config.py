import os
class Config():
    DEBUG = TESTING = True
    DATABASE_URI = "mysql+mysqlconnector://vinig79:vinig79@localhost/CRUD_FLASK"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SECRETY_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"