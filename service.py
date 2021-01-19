import db
def get_comics()-> list:
    #дергнуть database
    return db.get_comics()