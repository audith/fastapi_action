from sqlalchemy.orm import Session
from . import models,schemas

def create_user(db:Session,user:schemas.Usercreate):
    db_user=models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db:Session):
    return db.query(models.User).all()