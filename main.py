from app import app
from comics.view import comics
from character.view import characters

app.register_blueprint(comics, url_prefix='/')
app.register_blueprint(characters, url_prefix='/')

if __name__ == '__main__':
    app.run()
