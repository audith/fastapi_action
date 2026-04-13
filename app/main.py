from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from . import models,database,schemas,crud

models.Base.metadata.create_all(bind=database.engine)


app=FastAPI()

@app.post("/users",response_model=schemas.Usercreate)
def create_user(user:schemas.Usercreate,db:Session=Depends(database.get_db)):
    return crud.create_user(db,user)


@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(database.get_db)):
    users = crud.get_users(db)
    return users
