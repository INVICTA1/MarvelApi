import db



def get_comics() -> list:
    # дергнуть database
    return db.get_comics()


def add_comics(comic) :
    return db.add_comics(comic)
