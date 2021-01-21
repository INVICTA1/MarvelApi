from app import app
from comics.view import comics
from character.view import characters
from creators.view import creators

app.register_blueprint(comics)
app.register_blueprint(characters)
app.register_blueprint(creators)


if __name__ == '__main__':
    app.run()
