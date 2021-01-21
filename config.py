class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost:3306/marvel'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False