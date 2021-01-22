from src.app import app
from src.comics.view import comics
from src.character.view import characters
from src.creators.view import creators

app.register_blueprint(comics)
app.register_blueprint(characters)
app.register_blueprint(creators)


if __name__ == '__main__':
    app.run()
