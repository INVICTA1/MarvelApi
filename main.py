from app import app
from view import comics

app.register_blueprint(comics,url_prefix='/')
if __name__ == '__main__':
    app.run()
